#!/usr/bin/env python3
"""Generate finished content (Jimmy) from Donald nugget export JSON.

This is a robust, script-based runner to avoid cron agentTurns wedging.
It uses `openclaw agent --agent jimmy --local` (runs embedded locally).

Inputs:
- nuggets JSON file path
- run_id
Outputs:
- finished markdown in ~/krc_vault/finished content for posting/
- uploads to Drive via gog
- updates manifest drive link

Requirements:
- openclaw CLI configured with model access for --local (if not available, this script will fail).
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
from pathlib import Path

# Ensure krc scripts folder is importable (for run_helpers)
import sys
sys.path.insert(0, '/home/openclaw_agent_1/.openclaw/scripts/krc')

VAULT_ROOT = Path(os.path.expanduser(os.environ.get('KRC_VAULT_ROOT', '~/krc_vault')))
FINISHED_DIR = VAULT_ROOT / 'finished content for posting'
MANIFEST_DIR = VAULT_ROOT / 'manifests'
DRIVE_FOLDER_ID = '1NOCxQ2K1S2vM07hGHc0xEqTrsl2Ub1tv'


def load_json(p: Path):
    return json.loads(p.read_text())


def save_json(p: Path, obj):
    p.write_text(json.dumps(obj, indent=2, ensure_ascii=False))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('nuggets_json')
    ap.add_argument('--run-id', required=True)
    ap.add_argument('--client', default='Unknown')
    ap.add_argument('--jimmy-agent', default=os.environ.get('KRC_JIMMY_AGENT', 'jimmy'))
    args = ap.parse_args()

    nuggets_path = Path(args.nuggets_json)
    if not nuggets_path.exists():
        print(json.dumps({'ok': False, 'error': 'nuggets_json not found', 'path': str(nuggets_path)}))
        return 2

    run_id = args.run_id
    manifest_path = MANIFEST_DIR / f'{run_id}__manifest.json'
    if not manifest_path.exists():
        print(json.dumps({'ok': False, 'error': 'manifest missing', 'run_id': run_id}))
        return 3

    # Ask Jimmy to write finished content following his strict contract.
    nuggets_obj = load_json(nuggets_path)
    prompt = {
        'run_id': run_id,
        'client': args.client,
        'instruction': (
            'Generate finished content markdown. Output must be ONLY the finished content markdown (no code fences). '\
            'It MUST include a line starting with "CAPTION:" followed by a clear, scannable title line (5-12 words) on the next line.'
        ),
        'nuggets_export': nuggets_obj,
    }

    # Run Jimmy locally through embedded agent.
    cmd = [
        'openclaw','agent',
        '--agent', args.jimmy_agent,
        '--local',
        '--timeout','900',
        '--message', json.dumps(prompt, ensure_ascii=False),
    ]
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        print(json.dumps({'ok': False, 'error': 'openclaw agent failed', 'stderr': p.stderr[-800:], 'stdout': p.stdout[-800:]}))
        return 4

    content = p.stdout
    if not content.strip():
        print(json.dumps({'ok': False, 'error': 'empty output from jimmy'}))
        return 5
    if 'CAPTION:' not in content:
        print(json.dumps({'ok': False, 'error': 'jimmy output missing CAPTION marker'}))
        return 5

    FINISHED_DIR.mkdir(parents=True, exist_ok=True)
    finished_path = FINISHED_DIR / f'{run_id}__finished_content.md'
    finished_path.write_text(content, encoding='utf-8')

    # Upload to Drive as a Google Doc (use a scannable name)
    from run_helpers import infer_drive_doc_name  # local helper
    doc_name = infer_drive_doc_name(run_id, str(finished_path), client=args.client)

    up = subprocess.run(
        ['gog','drive','upload', str(finished_path), '--parent', DRIVE_FOLDER_ID, '--convert-to','doc', '--name', doc_name, '--json','--results-only','--no-input'],
        capture_output=True,
        text=True,
    )
    if up.returncode != 0:
        print(json.dumps({'ok': False, 'error': 'drive upload failed', 'stderr': up.stderr[-800:]}))
        return 6

    meta = json.loads(up.stdout)
    file_meta = meta.get('file') or meta
    link = file_meta.get('webViewLink')
    file_id = file_meta.get('id')

    m = load_json(manifest_path)
    m.setdefault('drive', {})
    m['drive'].update({'file_id': file_id, 'folder_id': DRIVE_FOLDER_ID, 'link': link, 'format': 'google_doc'})
    # Ensure finished content is recorded
    m['finished_content_file(s)'] = [str(finished_path)]
    save_json(manifest_path, m)

    print(json.dumps({'ok': True, 'run_id': run_id, 'drive_link': link, 'file_id': file_id, 'finished_path': str(finished_path)}))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
