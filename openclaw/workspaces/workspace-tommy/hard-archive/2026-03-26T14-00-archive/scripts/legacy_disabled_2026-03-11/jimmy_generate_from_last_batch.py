#!/usr/bin/env python3
"""Generate Jimmy finished drafts for the latest batch.

Reads last_batch.json, picks REAL nuggets files (largest) per run_id, runs
jimmy_generate_from_nuggets.py for each.

Outputs JSON with drive links.
"""

from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path


def main() -> int:
    last = Path(os.path.expanduser('~/krc_vault/fathom_library/state/last_batch.json'))
    if not last.exists():
        print(json.dumps({'ok': False, 'error': 'last_batch.json missing'}))
        return 2

    batch = json.loads(last.read_text())
    out = {'ok': True, 'results': []}

    for r in (batch.get('results') or []):
        if not r.get('ok'):
            continue
        run_id = r.get('run_id')
        client = r.get('client') or 'Unknown'
        if not run_id:
            continue

        # pick largest nuggets json for run_id
        cand_dir = Path(os.path.expanduser('~/krc_vault/gold nugget exports'))
        cands = sorted(cand_dir.glob(f"{run_id}__*__nuggets.json"), key=lambda p: p.stat().st_size, reverse=True)
        if not cands:
            out['ok'] = False
            out['results'].append({'run_id': run_id, 'client': client, 'ok': False, 'error': 'no nuggets json found'})
            continue

        nuggets = str(cands[0])
        cmd = ['python3','/home/openclaw_agent_1/.openclaw/scripts/krc/jimmy_generate_from_nuggets.py', nuggets, '--run-id', run_id, '--client', client]
        p = subprocess.run(cmd, capture_output=True, text=True)
        if p.returncode != 0:
            out['ok'] = False
            out['results'].append({'run_id': run_id, 'client': client, 'ok': False, 'error': p.stderr[-400:] or p.stdout[-400:]})
            continue

        try:
            j = json.loads((p.stdout or '').strip() or '{}')
        except Exception:
            j = {'ok': False, 'error': 'non-json output', 'stdout': (p.stdout or '')[-400:]}

        out['results'].append({'run_id': run_id, 'client': client, **j})

    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0 if out['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
