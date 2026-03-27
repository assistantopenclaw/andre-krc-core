#!/usr/bin/env python3
"""Run Jimmy on the most recent fathom library batch.

Reads:
- ~/krc_vault/fathom_library/state/last_batch.json

For each ok=true result:
- Uses nugget_export path from last_batch (or derives from run_id)
- Runs jimmy_process_export.py

Outputs JSON summary.
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
    results = []
    ok_all = True

    for r in (batch.get('results') or []):
        if not r.get('ok'):
            continue
        run_id = r.get('run_id')
        export_path = r.get('nugget_export')
        if not export_path and run_id:
            # fallback: find any nugget file matching run_id
            cand_dir = Path(os.path.expanduser('~/krc_vault/gold nugget exports'))
            cands = sorted(cand_dir.glob(f"{run_id}__*__nuggets.json"))
            export_path = str(cands[0]) if cands else None

        if not export_path or not Path(export_path).exists():
            ok_all = False
            results.append({'run_id': run_id, 'ok': False, 'error': f'export not found: {export_path}'})
            continue

        cmd = ['python3', '/home/openclaw_agent_1/.openclaw/scripts/krc/jimmy_process_export.py', export_path]
        p = subprocess.run(cmd, capture_output=True, text=True)
        item = {
            'run_id': run_id,
            'export': export_path,
            'ok': p.returncode == 0,
            'returncode': p.returncode,
            'stderr': (p.stderr or '')[:400],
        }
        if not item['ok']:
            ok_all = False
        results.append(item)

    print(json.dumps({'ok': ok_all, 'results': results}, indent=2))
    return 0 if ok_all else 1


if __name__ == '__main__':
    raise SystemExit(main())
