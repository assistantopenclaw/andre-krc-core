#!/usr/bin/env python3
"""Build a lunch digest from the most recent Fathom library batch.

Reads:
- ~/krc_vault/fathom_library/state/last_batch.json
- ~/krc_vault/manifests/<run_id>__manifest.json

Outputs plain text:
- one line per run with client + Drive link if present
"""

from __future__ import annotations

import json
import os
from pathlib import Path


def main() -> int:
    last = Path(os.path.expanduser('~/krc_vault/fathom_library/state/last_batch.json'))
    if not last.exists():
        print('LUNCH DIGEST: no last_batch.json found')
        return 2

    batch = json.loads(last.read_text())
    results = batch.get('results') or []

    lines = []
    lines.append('Lunch drafts (latest batch):')

    any_link = False
    for r in results:
        run_id = r.get('run_id')
        client = r.get('client') or 'Unknown'
        if not run_id:
            continue
        mp = Path(os.path.expanduser(f'~/krc_vault/manifests/{run_id}__manifest.json'))
        link = None
        if mp.exists():
            m = json.loads(mp.read_text())
            link = (m.get('drive') or {}).get('link')
        if link:
            any_link = True
            lines.append(f'- {client} | {link}')
        else:
            lines.append(f'- {client} | {run_id} | (no Drive link yet)')

    if not any_link:
        lines.append('')
        lines.append('Note: No Drive links found yet. Jimmy upload step may not have run or may have failed.')

    print('\n'.join(lines))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
