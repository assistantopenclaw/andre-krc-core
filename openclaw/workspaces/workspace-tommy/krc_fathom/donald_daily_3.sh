#!/usr/bin/env bash
set -euo pipefail

# Process next 3 unprocessed Fathom calls from the library.
# Uses donald_process_url.py to fetch transcript + run Donald nugget extraction pipeline.

INDEX_JSON="$HOME/krc_vault/fathom_library/index.json"
STATE_DIR="$HOME/krc_vault/fathom_library/state"
STATE_FILE="$STATE_DIR/processed.json"
LOG_DIR="$HOME/krc_vault/fathom_library/state/logs"

mkdir -p "$STATE_DIR" "$LOG_DIR"

if [[ ! -f "$STATE_FILE" ]]; then
  echo '{"processed":[],"updated_at":null}' > "$STATE_FILE"
fi

python3 - <<'PY'
import json, os, subprocess, datetime
from pathlib import Path

index_path=Path(os.path.expanduser('~/krc_vault/fathom_library/index.json'))
state_path=Path(os.path.expanduser('~/krc_vault/fathom_library/state/processed.json'))

idx=json.loads(index_path.read_text())
state=json.loads(state_path.read_text())
processed=set(state.get('processed') or [])

# oldest-first so we steadily chew through backlog
pending=[r for r in idx if (r.get('share_url') and r['share_url'] not in processed)]

take=pending[:3]

out={'selected': take, 'count_selected': len(take), 'pending_total': len(pending)}
print(json.dumps(out, indent=2))

for r in take:
    url=r['share_url']
    # Run Donald pipeline (REPROCESS disabled; we want idempotence by manifest success check)
    cmd=['python3','/home/openclaw_agent_1/.openclaw/scripts/krc/donald_process_url.py', url]
    p=subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode not in (0,2):
        raise SystemExit(f"donald_process_url failed rc={p.returncode} url={url} stderr={p.stderr[:500]}")
    processed.add(url)

state['processed']=sorted(processed)
state['updated_at']=datetime.datetime.now(datetime.timezone.utc).isoformat()
state_path.write_text(json.dumps(state, indent=2))
PY
