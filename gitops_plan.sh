#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "Usage: $0 <manifest.tsv>" >&2
  exit 1
fi

MANIFEST="$1"
ROOT_REPO="/home/openclaw_agent_1/.openclaw/scripts"

if [ ! -f "$MANIFEST" ]; then
  echo "Manifest not found: $MANIFEST" >&2
  exit 2
fi

while IFS=$'\t' read -r SRC DEST; do
  [ -z "${SRC:-}" ] && continue
  [ "${SRC#\#}" != "$SRC" ] && continue
  ABS_SRC="$ROOT_REPO/$SRC"
  echo "=== $SRC -> $DEST ==="
  if [ -f "$DEST" ] && [ -f "$ABS_SRC" ]; then
    diff -u "$DEST" "$ABS_SRC" || true
  else
    echo "Target missing or source missing; full copy needed."
  fi
  echo
done < "$MANIFEST"
