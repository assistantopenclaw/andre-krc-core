#!/bin/bash
# /home/openclaw_agent_1/.openclaw/scripts/daily_backup.sh
# Simple, reliable local backup script for OpenClaw.

set -e

BACKUP_ROOT="/home/openclaw_agent_1/.openclaw/backups"
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)
DEST="$BACKUP_ROOT/$TIMESTAMP"

# Ensure backup root exists
mkdir -p "$BACKUP_ROOT"
mkdir -p "$DEST"

echo "Starting local backup to $DEST..."

# 1. Back up main config
if [ -f "/home/openclaw_agent_1/.openclaw/openclaw.json" ]; then
  cp "/home/openclaw_agent_1/.openclaw/openclaw.json" "$DEST/"
  echo "- Saved openclaw.json"
fi

# 2. Back up all agent memories and workspaces (MD files and JSON)
# We loop through all workspace directories found in .openclaw
for ws in /home/openclaw_agent_1/.openclaw/workspace*; do
  if [ -d "$ws" ]; then
    # Determine a clean name for the folder
    folder_name=$(basename "$ws" | sed 's/workspace-//;s/workspace/main/')
    target_dir="$DEST/$folder_name"
    mkdir -p "$target_dir"
    
    # Copy all .md and .json files (non-recursive to keep it light/simple)
    find "$ws" -maxdepth 2 \( -name "*.md" -o -name "*.json" \) -exec cp {} "$target_dir/" \; 2>/dev/null || true
    
    # Also grab the memory subdirectory specifically
    if [ -d "$ws/memory" ]; then
      mkdir -p "$target_dir/memory"
      cp "$ws/memory/"*.md "$target_dir/memory/" 2>/dev/null || true
    fi
    echo "- Saved snapshot for $folder_name"
  fi
done

# 3. Handle local git rotation (if initialized)
if [ -d "$BACKUP_ROOT/.git" ]; then
  cd "$BACKUP_ROOT"
  git add "$TIMESTAMP" >/dev/null 2>&1 || true
  git -c user.name="BackupBot" -c user.email="backup@local" commit -m "Daily backup $TIMESTAMP" >/dev/null 2>&1 || true
fi

# 4. Retention Policy: Keep only the 7 most recent backup folders
# This prevents the disk from filling up over time.
ls -1dt "$BACKUP_ROOT"/*/ 2>/dev/null | tail -n +8 | xargs rm -rf 2>/dev/null || true

echo "Backup completed successfully at $(date)."
