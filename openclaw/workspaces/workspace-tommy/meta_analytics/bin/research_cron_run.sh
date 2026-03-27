#!/usr/bin/env bash
set -euo pipefail

# This script is invoked by the Research cron job.
# It must not prompt and must fail hard on any missing config.

export TZ="America/Chicago"

# Token can be provided either via env var (preferred) or via a protected file.
# File path lets cron run without embedding secrets in config.
TOKEN_FILE="/home/openclaw_agent_1/.openclaw/credentials/meta/system_user_token.txt"
if [[ -z "${META_SYSTEM_USER_TOKEN:-}" ]]; then
  if [[ -f "$TOKEN_FILE" ]]; then
    export META_SYSTEM_USER_TOKEN="$(cat "$TOKEN_FILE" | tr -d '\r' | tr -d '\n')"
  fi
fi

: "${META_SYSTEM_USER_TOKEN:?META_SYSTEM_USER_TOKEN is required (set env or create $TOKEN_FILE)}"

# Folder: Openclaw Content Analytics
export GDRIVE_CONTENT_ANALYTICS_FOLDER_ID="${GDRIVE_CONTENT_ANALYTICS_FOLDER_ID:-17vjnPR3hiwYu5dd0OMQiugZ9IAV-XiGE}"

# Optional pinning. If unset, the run will discover the first page.
# export META_PAGE_ID="..."
# export META_PREFERRED_PAGE_NAME="..."

SCRIPT_DIR="/home/openclaw_agent_1/.openclaw/workspace-tommy/meta_analytics/bin"

# Run and capture output for deterministic error reporting.
OUT_JSON="$SCRIPT_DIR/.last_run.json"
ERR_TXT="$SCRIPT_DIR/.last_run.err"
set +e
python3 "$SCRIPT_DIR/meta_analytics_run.py" >"$OUT_JSON" 2>"$ERR_TXT"
CODE=$?
set -e

if [[ $CODE -eq 0 ]]; then
  cat "$OUT_JSON"
  exit 0
fi

# On failure: upload an error report doc to Drive so Andre always gets a readable artifact.
# Use ASCII-only titles to avoid Drive API 400 edge cases on conversion.
NOW_CT_HUMAN=$(TZ="America/Chicago" date '+%B %-d, %Y %-I:%M %p CT')
NOW_CT_SAFE=$(TZ="America/Chicago" date '+%Y-%m-%d_%H%M_CT')
TITLE="MetaFailure_${NOW_CT_SAFE}"
TMP_MD=$(mktemp --suffix=.md)
{
  # Avoid unicode em-dash; Drive conversion can 400 on some unicode.
  echo "# Meta Analytics Sweep Failure - ${NOW_CT_HUMAN}";
  echo;
  echo "## Error (raw)";
  echo '```json';
  cat "$OUT_JSON";
  echo;
  echo '```';
  if [[ -s "$ERR_TXT" ]]; then
    echo;
    echo "## STDERR";
    echo '```';
    sed -e 's/[[:cntrl:]]//g' "$ERR_TXT" | head -c 50000;
    echo;
    echo '```';
  fi
  echo;
  echo "## What to do";
  echo "- If this error contains: OAuthException / API access blocked => regenerate Meta System User token and replace the token file.";
} > "$TMP_MD"

# Upload error doc
UPLOAD_JSON=$(gog drive upload "$TMP_MD" --convert-to doc --parent "$GDRIVE_CONTENT_ANALYTICS_FOLDER_ID" --name "$TITLE" --json --results-only)

# Emit machine-readable summary (so the Research agent can announce the link)
python3 - <<PY
import json
u=json.loads('''$UPLOAD_JSON''')
print(json.dumps({
  'ok': False,
  'title': '$TITLE',
  'drive': {'id': u.get('id'), 'name': u.get('name'), 'webViewLink': u.get('webViewLink')},
  'exit_code': $CODE
}, indent=2))
PY

rm -f "$TMP_MD"
exit $CODE
