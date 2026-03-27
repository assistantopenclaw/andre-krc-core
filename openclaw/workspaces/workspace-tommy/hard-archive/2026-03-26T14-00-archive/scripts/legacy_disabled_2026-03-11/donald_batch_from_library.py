#!/usr/bin/env python3
"""Run a Donald batch from the local Fathom library.

Stage 1 goal: reliable throughput.
- Picks next N unprocessed share URLs.
- Runs donald_process_url.py for each (API fetch + transcript saved + manifest written).
- Marks them processed.
- Writes minimal nuggets/objections exports via donald_extract_from_manifest.py

Outputs JSON summary for cron delivery.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import subprocess
from pathlib import Path


def load_json(p: Path, default):
    if not p.exists():
        return default
    return json.loads(p.read_text())


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('--n', type=int, default=3)
    args = ap.parse_args()

    index_path = Path(os.path.expanduser('~/krc_vault/fathom_library/index.json'))
    state_dir = Path(os.path.expanduser('~/krc_vault/fathom_library/state'))
    state_path = state_dir / 'processed.json'
    state_dir.mkdir(parents=True, exist_ok=True)

    idx = load_json(index_path, [])
    state = load_json(state_path, {'processed': [], 'updated_at': None})
    processed = set(state.get('processed') or [])

    pending = [r for r in idx if r.get('share_url') and r['share_url'] not in processed]
    selected = pending[: max(0, args.n)]

    results = []
    ok_all = True

    for r in selected:
        url = r['share_url']
        cmd = ['python3', '/home/openclaw_agent_1/.openclaw/scripts/krc/donald_process_url.py', url]
        p = subprocess.run(cmd, capture_output=True, text=True)
        run_id = (p.stdout or '').strip().splitlines()[-1] if (p.stdout or '').strip() else None

        item = {
            'share_url': url,
            'client': r.get('client'),
            'created_at': r.get('created_at'),
            'meeting_title': r.get('meeting_title'),
            'ok': p.returncode in (0, 2),
            'returncode': p.returncode,
            'run_id': run_id,
            'stderr': (p.stderr or '')[:400],
            'nugget_export': None,
            'objection_export': None,
        }

        if item['ok'] and run_id:
            # Create minimal exports deterministically
            manifest = os.path.expanduser(f"~/krc_vault/manifests/{run_id}__manifest.json")
            cmd2 = ['python3', '/home/openclaw_agent_1/.openclaw/scripts/krc/donald_extract_from_manifest.py', manifest, '--client', (r.get('client') or 'Unknown')]
            p2 = subprocess.run(cmd2, capture_output=True, text=True)
            if p2.returncode == 0:
                try:
                    j = json.loads((p2.stdout or '{}').strip() or '{}')
                    item['nugget_export'] = j.get('nuggets')
                    item['objection_export'] = j.get('objections')
                except Exception:
                    pass
            else:
                item['ok'] = False
                item['stderr'] = ((item['stderr'] or '') + ' | extract_failed: ' + (p2.stderr or '')[:200]).strip()

        if item['ok']:
            processed.add(url)
        else:
            ok_all = False

        results.append(item)

    state['processed'] = sorted(processed)
    state['updated_at'] = dt.datetime.now(dt.timezone.utc).isoformat()
    state_path.write_text(json.dumps(state, indent=2))

    # Persist last batch for downstream jobs (Donald full extract, Jimmy drafts)
    last_batch_path = state_dir / 'last_batch.json'
    last_batch_path.write_text(json.dumps({
        'created_at': dt.datetime.now(dt.timezone.utc).isoformat(),
        'pending_total': len(pending),
        'selected_count': len(selected),
        'results': results,
    }, indent=2, ensure_ascii=False))


    out = {
        'ok': ok_all,
        'pending_total': len(pending),
        'selected_count': len(selected),
        'results': results,
        'state_file': str(state_path),
    }
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0 if ok_all else 1


if __name__ == '__main__':
    raise SystemExit(main())
