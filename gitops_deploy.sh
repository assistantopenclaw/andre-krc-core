#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <label> <manifest.tsv>" >&2
  exit 1
fi

LABEL="$1"
MANIFEST="$2"
ROOT_REPO="/home/openclaw_agent_1/.openclaw/scripts"
SAVEPOINT_TOOL="$ROOT_REPO/openclaw_surgery_savepoint.sh"
VERIFY_TOOL="$ROOT_REPO/openclaw_surgery_verify.sh"

if [ ! -f "$MANIFEST" ]; then
  echo "Manifest not found: $MANIFEST" >&2
  exit 2
fi

TARGETS=()
while IFS=$'\t' read -r SRC DEST; do
  [ -z "${SRC:-}" ] && continue
  [ "${SRC#\#}" != "$SRC" ] && continue
  TARGETS+=("$DEST")
done < "$MANIFEST"

if [ "${#TARGETS[@]}" -eq 0 ]; then
  echo "No targets in manifest" >&2
  exit 3
fi

SAVEPOINT_OUTPUT="$($SAVEPOINT_TOOL "$LABEL" "${TARGETS[@]}")"
echo "$SAVEPOINT_OUTPUT"
ROLLBACK_CMD="$(printf '%s\n' "$SAVEPOINT_OUTPUT" | awk -F': ' '/Rollback command:/ {print $2}')"

while IFS=$'\t' read -r SRC DEST; do
  [ -z "${SRC:-}" ] && continue
  [ "${SRC#\#}" != "$SRC" ] && continue
  ABS_SRC="$ROOT_REPO/$SRC"
  mkdir -p "$(dirname "$DEST")"
  cp -a "$ABS_SRC" "$DEST"
done < "$MANIFEST"

$VERIFY_TOOL

echo "Deploy complete."
echo "Rollback command: $ROLLBACK_CMD"
