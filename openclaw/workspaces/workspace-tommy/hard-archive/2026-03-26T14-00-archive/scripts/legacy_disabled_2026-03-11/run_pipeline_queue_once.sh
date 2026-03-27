#!/usr/bin/env bash
set -euo pipefail

VAULT_ROOT="${KRC_VAULT_ROOT:-/home/openclaw_agent_1/krc_vault}"
QUEUE_DIR="$VAULT_ROOT/queue"
PENDING="$QUEUE_DIR/pending_links.txt"
INPROG="$QUEUE_DIR/in_progress"
DONE="$QUEUE_DIR/done"
FAILED="$QUEUE_DIR/failed"
PIPELINE="/home/openclaw_agent_1/.openclaw/scripts/krc/run_pipeline_one_lane.py"
BATCH_COUNT="${BATCH_COUNT:-1}"

mkdir -p "$QUEUE_DIR" "$INPROG" "$DONE" "$FAILED" "$VAULT_ROOT/google_drive_exports"
[[ -f "$PENDING" ]] || touch "$PENDING"

lock="$QUEUE_DIR/queue.lock"
exec 9>"$lock"
flock -n 9 || exit 0

processed=0
while [[ "$processed" -lt "$BATCH_COUNT" ]]; do
  # atomically pop first non-empty line
  link=""
  tmp=$(mktemp)
  while IFS= read -r line || [ -n "$line" ]; do
    if [[ -z "$link" && -n "${line// /}" ]]; then
      link="$line"
    else
      echo "$line" >> "$tmp"
    fi
  done < "$PENDING"
  mv "$tmp" "$PENDING"

  [[ -z "$link" ]] && break

  ts=$(date +%Y%m%d_%H%M%S)
  infile="$INPROG/${ts}.link"
  printf '%s\n' "$link" > "$infile"

  set +e
  out=$(KRC_VAULT_ROOT="$VAULT_ROOT" KRC_JIMMY_AGENT="${KRC_JIMMY_AGENT:-jimmy}" python3 "$PIPELINE" "$link" 2>&1)
  rc=$?
  set -e

  run_id=$(echo "$out" | sed -n 's/^RUN_ID=\([^ ]*\).*/\1/p' | head -n1)
  status=$(echo "$out" | sed -n 's/^RUN_ID=[^ ]* status=\([^ ]*\).*/\1/p' | head -n1)
  posts=$(echo "$out" | sed -n 's/^RUN_ID=[^ ]* status=[^ ]* posts_exported=\([^ ]*\).*/\1/p' | head -n1)
  exp=$(echo "$out" | sed -n 's/^RUN_ID=[^ ]* status=[^ ]* posts_exported=[^ ]* export_path=\(.*\)$/\1/p' | head -n1)

  if [[ $rc -eq 0 && "$status" == "ok" ]]; then
    mv "$infile" "$DONE/${run_id}_${ts}.link"
    openclaw message send --channel telegram --account tommy --target 8434682557 --message "RUN_ID=${run_id} status=ok posts_exported=${posts:-0} export_path=${exp:-$VAULT_ROOT/google_drive_exports}" >/dev/null 2>&1 || true
  else
    reason=$(echo "$out" | tail -n1 | tr '\n' ' ' | cut -c1-180)
    mv "$infile" "$FAILED/${run_id:-unknown}_${ts}__${reason//[^A-Za-z0-9._-]/_}.link"
    openclaw message send --channel telegram --account tommy --target 8434682557 --message "RUN_ID=${run_id:-unknown} status=fail posts_exported=0 export_path=$VAULT_ROOT/google_drive_exports" >/dev/null 2>&1 || true
  fi

  processed=$((processed+1))
done

remaining=$(grep -cve '^\s*$' "$PENDING" || true)
openclaw message send --channel telegram --account tommy --target 8434682557 --message "QUEUE_BATCH_DONE processed=${processed} remaining=${remaining}" >/dev/null 2>&1 || true
