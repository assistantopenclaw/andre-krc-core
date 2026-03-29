#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <label> <target1> [target2 ...]" >&2
  exit 1
fi

LABEL_RAW="$1"
shift

SAFE_LABEL="$(printf '%s' "$LABEL_RAW" | tr '[:upper:]' '[:lower:]' | tr -cs 'a-z0-9._-' '-')"
TS="$(date +%Y%m%d-%H%M%S)"
ROOT="$HOME/.openclaw/surgery-savepoints/${TS}_${SAFE_LABEL}"
FILES_DIR="$ROOT/files"
TARGETS_FILE="$ROOT/TARGETS.txt"
META_FILE="$ROOT/METADATA.txt"
ROLLBACK_FILE="$ROOT/ROLLBACK.sh"
LATEST_LINK="$HOME/.openclaw/surgery-savepoints/latest"
LATEST_CMD_FILE="$HOME/.openclaw/surgery-savepoints/LATEST_ROLLBACK_COMMAND.txt"

mkdir -p "$FILES_DIR"
: > "$TARGETS_FILE"

NEEDS_GATEWAY_RESTART=0

for target in "$@"; do
  ABS="$(readlink -f "$target")"
  if [ ! -e "$ABS" ]; then
    echo "Missing target: $target" >&2
    exit 2
  fi
  REL="${ABS#/}"
  DEST="$FILES_DIR/$REL"
  mkdir -p "$(dirname "$DEST")"
  cp -a "$ABS" "$DEST"
  printf '%s\n' "$ABS" >> "$TARGETS_FILE"

  case "$ABS" in
    */.openclaw/openclaw.json|*.service)
      NEEDS_GATEWAY_RESTART=1
      ;;
  esac
done

cat > "$ROLLBACK_FILE" <<EOF
#!/usr/bin/env bash
set -euo pipefail
ROOT="$ROOT"
FILES_DIR="\$ROOT/files"
TARGETS_FILE="\$ROOT/TARGETS.txt"
NEEDS_GATEWAY_RESTART="$NEEDS_GATEWAY_RESTART"

while IFS= read -r TARGET; do
  [ -z "\$TARGET" ] && continue
  REL="\${TARGET#/}"
  SRC="\$FILES_DIR/\$REL"

  if [ -d "\$SRC" ]; then
    rm -rf "\$TARGET"
    mkdir -p "$(dirname "\$TARGET")"
    cp -a "\$SRC" "\$TARGET"
  else
    mkdir -p "$(dirname "\$TARGET")"
    cp -a "\$SRC" "\$TARGET"
  fi
done < "\$TARGETS_FILE"

if [ "\$NEEDS_GATEWAY_RESTART" = "1" ]; then
  openclaw gateway restart || true
fi

openclaw doctor || true
openclaw status || true

echo "Rollback complete from: \$ROOT"
EOF

chmod +x "$ROLLBACK_FILE"

cat > "$META_FILE" <<EOF
Label: $LABEL_RAW
Timestamp: $TS
Savepoint: $ROOT
Rollback command: bash "$ROLLBACK_FILE"
Needs gateway restart on rollback: $NEEDS_GATEWAY_RESTART

Targets:
$(cat "$TARGETS_FILE")
EOF

ln -sfn "$ROOT" "$LATEST_LINK"
printf 'bash "%s"\n' "$ROLLBACK_FILE" > "$LATEST_CMD_FILE"

echo "Savepoint created: $ROOT"
echo "Rollback command: bash \"$ROLLBACK_FILE\""
