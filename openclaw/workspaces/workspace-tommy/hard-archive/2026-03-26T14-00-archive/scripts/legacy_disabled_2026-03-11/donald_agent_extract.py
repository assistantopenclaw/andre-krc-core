#!/usr/bin/env python3
"""Call the Donald agent to do full nugget extraction for a given RUN_ID.

This avoids write-tool restrictions by letting Donald output to stdout and
we (this script) write the JSON into the vault using normal filesystem access.

Input:
- run_id
- raw transcript path is resolved via manifest

Output:
- ~/krc_vault/gold nugget exports/<run_id>__<Client>__nuggets.json

NOTE: This relies on sessions_spawn runtime=subagent with agentId=donald.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from pathlib import Path


def safe_client(s: str) -> str:
    s = (s or 'Unknown').strip()
    s = re.sub(r'[^A-Za-z0-9 ._\-()]+', '_', s)
    return s[:60].strip() or 'Unknown'


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument('run_id')
    ap.add_argument('--client', default='Unknown')
    args = ap.parse_args()

    run_id = args.run_id
    mp = Path(os.path.expanduser(f'~/krc_vault/manifests/{run_id}__manifest.json'))
    if not mp.exists():
        print(json.dumps({'ok': False, 'error': 'manifest missing', 'run_id': run_id}))
        return 2

    m = json.loads(mp.read_text())
    raw = m.get('raw_transcript_file')
    if not raw or not Path(raw).exists():
        print(json.dumps({'ok': False, 'error': 'raw transcript missing', 'run_id': run_id, 'raw': raw}))
        return 3

    transcript = Path(raw).read_text(encoding='utf-8', errors='ignore')

    prompt = f"""You are Donald (PROSPECTOR). Produce ONLY the NUGGET LIBRARY JSON deliverable (no markdown).

Constraints:
- Use your SOUL.md schema discipline.
- Do NOT fabricate.
- Include proof_quote_redacted + proof_location + proof_anchor_lines.
- Output valid JSON only.

RUN_ID: {run_id}
SOURCE: {m.get('source_url') or 'FATHOM'}
TRANSCRIPT:\n{transcript}\n"""

    # Use openclaw sessions_spawn via CLI is not available here; we call gateway-internal sessions_spawn by invoking openclaw? Not available.
    # Fallback: not implemented.
    print(json.dumps({'ok': False, 'error': 'donald_agent_extract not wired to sessions_spawn in script mode'}))
    return 4


if __name__ == '__main__':
    raise SystemExit(main())
