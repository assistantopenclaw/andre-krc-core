#!/bin/bash
# Script to send reminder to Andre via OpenClaw message CLI (or adjust to your environment).
# Expected: `openclaw message send --target telegram:8434682557 --message "go get Tommy drinks"`
# If your environment uses a different CLI or requires a bot token, edit this script accordingly.

# Message text
MSG="go get Tommy drinks"

# Preferred: use OpenClaw CLI if available
if command -v openclaw >/dev/null 2>&1; then
  openclaw message send --target telegram:8434682557 --message "$MSG"
  exit $?
fi

# Fallback: try curl with TELEGRAM_BOT_TOKEN env var
if [ -n "$TELEGRAM_BOT_TOKEN" ]; then
  CHAT_ID="8434682557"
  curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" -d chat_id="$CHAT_ID" -d text="$MSG"
  exit $?
fi

# If neither method exists, log to a file for manual action
echo "[$(date -u +%Y-%m-%dT%H:%M:%SZ)] Remind: $MSG" >> ~/tommy_drinks_reminder_fallback.log
exit 0
