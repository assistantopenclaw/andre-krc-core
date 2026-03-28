#!/bin/bash
# Manager → R2 Fathom Relay
# Background listener: checks for new Fathom URLs sent to Manager's Telegram bot
# and forwards them to R2 for processing.
# Run via cron every 5 minutes OR as a persistent background job.

TELEGRAM_MANAGER_API="https://api.telegram.org/bot8549777930:AAGpusN9_F_JHIBibSyUXbs-rBCIV5uHtPg"
TELEGRAM_R2_API="https://api.telegram.org/bot8687062381:AAFaXtgkif9fX7b7uok0QgFF4wZQRnNGffI"
CHAT_ID="8434682557"
PROCESSED_FILE="/tmp/fathom_urls_processed.txt"
OFFSET_FILE="/tmp/manager_telegram_offset.txt"
POLL_INTERVAL=30  # seconds between checks

# Track last processed message offset
if [ -f "$OFFSET_FILE" ]; then
  OFFSET=$(cat "$OFFSET_FILE")
else
  OFFSET=0
fi

# Get updates since last offset
RESPONSE=$(curl -s "${TELEGRAM_MANAGER_API}/getUpdates?offset=$((OFFSET + 1))&timeout=5&limit=1" 2>/dev/null)

if [ -z "$RESPONSE" ] || [ "$(echo "$RESPONSE" | head -c 20)" = "{\"ok\":false" ]; then
  exit 0
fi

# Check for new messages from Andre with Fathom URLs
UPDATES=$(echo "$RESPONSE" | python3 -c "
import sys,json
d=json.load(sys.stdin)
updates = d.get('result', [])
for u in updates:
    msg = u.get('message', {})
    chat_id = msg.get('chat', {}).get('id')
    text = msg.get('text', '') or msg.get('caption', '') or ''
    msg_id = u.get('update_id')
    print(f'ID:{msg_id} CHAT:{chat_id} TEXT:{text[:200]}')
" 2>/dev/null || echo "")

# Check each update for Fathom URL
FOUND=0
NEW_OFFSET=$OFFSET
while IFS= read -r line; do
  [ -z "$line" ] && continue
  MSG_ID=$(echo "$line" | grep -oP '^ID:\K\d+')
  CHAT=$(echo "$line" | grep -oP 'CHAT:\K\d+')
  TEXT=$(echo "$line" | sed 's/^ID:\d\+ CHAT:\d\+ TEXT://')
  
  # Update offset
  if [ -n "$MSG_ID" ] && [ "$MSG_ID" -gt "$NEW_OFFSET" ] 2>/dev/null; then
    NEW_OFFSET=$MSG_ID
  fi
  
  # Check if from Andre and contains Fathom URL
  if [ "$CHAT" = "$CHAT_ID" ] && echo "$TEXT" | grep -q "fathom\|zoom\.us\|teams.microsoft"; then
    # Skip if already processed
    if [ -f "$PROCESSED_FILE" ] && grep -q "$TEXT" "$PROCESSED_FILE" 2>/dev/null; then
      continue
    fi
    
    FOUND=1
    echo "[$(date)] Found Fathom URL: $TEXT" >> /tmp/fathom_relay_log.txt
    echo "$TEXT" >> "$PROCESSED_FILE"
    
    # Forward to R2 via R2's Telegram bot with instruction
    FORWARD_MSG="📋 New evening review recording received from Andre.

Fathom URL: $TEXT

R2 — please process this recording:
1. Fetch transcript from Fathom
2. Summarize: wins, shortfalls, root causes, priorities, patterns
3. Update Andre's user profile and daily memory
4. Confirm when done."

    curl -s -X POST "${TELEGRAM_R2_API}/sendMessage" \
      -d "chat_id=${CHAT_ID}" \
      -d "text=${FORWARD_MSG}" \
      -d "disable_notification=false" > /dev/null 2>&1
    
    echo "[$(date)] Forwarded to R2" >> /tmp/fathom_relay_log.txt
  fi
done <<< "$UPDATES"

# Save new offset
echo "$NEW_OFFSET" > "$OFFSET_FILE"
