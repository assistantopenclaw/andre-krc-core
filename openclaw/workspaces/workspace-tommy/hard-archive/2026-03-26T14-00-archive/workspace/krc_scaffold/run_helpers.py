import hashlib
import json
import os
import re
from datetime import datetime, timezone

VAULT = os.path.expanduser('~/krc_vault')
RAW_DIR = os.path.join(VAULT, 'raw call transcripts')
NUGGET_DIR = os.path.join(VAULT, 'gold nugget exports')
FINISHED_DIR = os.path.join(VAULT, 'finished content for posting')
LOG_DIR = os.path.join(VAULT, 'run logs')
MANIFEST_DIR = os.path.join(VAULT, 'manifests')

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


def find_existing_success(url: str):
    """Return run_id if url_hash already processed successfully."""
    uh = url_hash(url)
    if not os.path.isdir(MANIFEST_DIR):
        return None
    for name in os.listdir(MANIFEST_DIR):
        if not name.endswith('__manifest.json'):
            continue
        p = os.path.join(MANIFEST_DIR, name)
        try:
            with open(p, 'r', encoding='utf-8') as f:
                m = json.load(f)
            if m.get('url_hash') == uh and m.get('status') == 'success':
                return m.get('run_id')
        except Exception:
            continue
    return None
