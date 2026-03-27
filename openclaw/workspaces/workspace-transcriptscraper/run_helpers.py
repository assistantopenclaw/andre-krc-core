import hashlib
import json
import os
import re
from pathlib import Path
from datetime import datetime, timezone

VAULT = os.path.expanduser(os.environ.get('KRC_VAULT_ROOT', '~/krc_vault'))
RAW_DIR = os.path.join(VAULT, 'raw call transcripts')
NUGGET_DIR = os.path.join(VAULT, 'gold nugget exports')
FINISHED_DIR = os.path.join(VAULT, 'finished content for posting')
LOG_DIR = os.path.join(VAULT, 'run logs')
MANIFEST_DIR = os.path.join(VAULT, 'manifests')

# Google Drive folder for finished content (OpenClaw Finished Content)
FINISHED_DRIVE_FOLDER_ID = '1NOCxQ2K1S2vM07hGHc0xEqTrsl2Ub1tv'

ALLOWED_DOMAIN_SUBSTR_DEFAULT = 'fathom'


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def short_hash(s: str, n: int = 8) -> str:
    return hashlib.sha256(s.encode('utf-8')).hexdigest()[:n]


def url_hash(url: str) -> str:
    return hashlib.sha256(url.encode('utf-8')).hexdigest()


def new_run_id(url: str) -> str:
    ts = datetime.now().strftime('%Y%m%d_%H%M%S')
    return f"{ts}_{short_hash(url, 8)}"


def sanitize_filename(s: str, max_len: int = 80) -> str:
    s = re.sub(r'https?://', '', s)
    s = re.sub(r'[^A-Za-z0-9._-]+', '_', s)
    s = s.strip('_')
    if len(s) > max_len:
        s = s[:max_len]
    return s or 'untitled'


def manifest_path(run_id: str) -> str:
    return os.path.join(MANIFEST_DIR, f"{run_id}__manifest.json")


def log_path(run_id: str) -> str:
    return os.path.join(LOG_DIR, f"{run_id}__log.txt")


def load_manifest(run_id: str):
    p = manifest_path(run_id)
    if not os.path.exists(p):
        return None
    with open(p, 'r', encoding='utf-8') as f:
        return json.load(f)


def write_manifest(m: dict):
    os.makedirs(MANIFEST_DIR, exist_ok=True)
    m['updated_at'] = now_iso()
    if 'created_at' not in m:
        m['created_at'] = m['updated_at']
    with open(manifest_path(m['run_id']), 'w', encoding='utf-8') as f:
        json.dump(m, f, indent=2, ensure_ascii=False)


def append_log(run_id: str, line: str):
    os.makedirs(LOG_DIR, exist_ok=True)
    with open(log_path(run_id), 'a', encoding='utf-8') as f:
        f.write(line.rstrip('\n') + '\n')


def _is_usable_success_manifest(m: dict) -> bool:
    """Success manifests are usable only if required artifact paths exist."""
    if (m or {}).get('status') != 'success':
        return False
    raw = (m or {}).get('raw_transcript_file')
    nug = (m or {}).get('nugget_export_file')
    if not raw or not nug:
        return False
    return os.path.exists(raw) and os.path.exists(nug)


def find_existing_success(url: str):
    """Return best usable prior success run_id for this URL hash, else None.

    A prior run only counts as success for idempotency if its core artifacts exist.
    """
    uh = url_hash(url)
    if not os.path.isdir(MANIFEST_DIR):
        return None

    candidates: list[tuple[float, str]] = []
    for name in os.listdir(MANIFEST_DIR):
        if not name.endswith('__manifest.json'):
            continue
        p = os.path.join(MANIFEST_DIR, name)
        try:
            with open(p, 'r', encoding='utf-8') as f:
                m = json.load(f)
            if m.get('url_hash') != uh:
                continue
            if not _is_usable_success_manifest(m):
                continue
            # Prefer latest by manifest mtime.
            candidates.append((os.path.getmtime(p), m.get('run_id')))
        except Exception:
            continue

    if not candidates:
        return None
    candidates.sort(reverse=True)
    return candidates[0][1]


def infer_drive_doc_name(run_id: str, finished_md_path: str, client: str | None = None, max_len: int = 120) -> str:
    """Create a human-readable Google Doc name for Drive.

    Goal: make Drive list scannable.

    Format:
      <Client> — <First caption line> (<run_id suffix>)

    - Extracts first non-empty line after 'CAPTION:' in the finished content file.
    - Collapses whitespace and truncates.
    """
    title = None
    try:
        content = Path(finished_md_path).read_text(encoding='utf-8', errors='ignore')
        idx = content.find('CAPTION:')
        if idx != -1:
            after = content[idx + len('CAPTION:'):].lstrip('\n ').splitlines()
            for line in after:
                s = line.strip()
                if not s:
                    continue
                # Skip obvious headings/labels
                if s.upper() in {'NOTES:', 'CAPTION:', 'OVERLAY_CTA:', 'OVERLAY_HOOK_1:', 'OVERLAY_HOOK_2:', 'OVERLAY_HOOK_3:'}:
                    continue
                if s.startswith('#') or s.startswith('##') or s.startswith('---'):
                    continue
                s = re.sub(r'\s+', ' ', s)
                title = s
                break
    except Exception:
        title = None

    if not title:
        title = 'Finished Content'

    # Try to include client for scanability
    client_part = None
    if client:
        client_part = sanitize_filename(client, max_len=40).replace('_', ' ').strip()
    if client_part:
        # use last 8 of run_id to avoid repeating date prefix everywhere
        suffix = run_id[-8:]
        name = f"{client_part} — {title} ({suffix})"
    else:
        name = f"{run_id}: {title}"

    name = re.sub(r'\s+', ' ', name).strip()
    return name[:max_len]
