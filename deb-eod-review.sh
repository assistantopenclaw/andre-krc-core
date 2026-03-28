#!/bin/bash
# EOD Review Script — Manager Agent
# Fires at 7 PM CT daily
# Sends structured evening review to Andre via Telegram

set -e

GOG_KEYRING_BACKEND=file
GOG_KEYRING_PASSWORD="s7C3Kdr9AgUvh9jkVOL9VqxvUfy7e_TkwBa0gbyNga0"
export GOG_KEYRING_BACKEND GOG_KEYRING_PASSWORD

ANDRE_ACCOUNT="andre@kingdomrelationshipcoaching.com"
TELEGRAM_API="https://api.telegram.org/bot8549777930:AAGpusN9_F_JHIBibSyUXbs-rBCIV5uHtPg"
CHAT_ID="8434682557"
TODAY=$(date +%Y-%m-%d)
YESTERDAY=$(date -d "yesterday" +%Y-%m-%d)
TODAY_CT=$(date +"%A, %B %d")
GOALS_FILE="/tmp/eod_goals_${TODAY}.txt"

# --- CALENDAR (today's events) ---
RAW_CAL=$(GOG_KEYRING_BACKEND=file GOG_KEYRING_PASSWORD="$GOG_KEYRING_PASSWORD" \
  gog calendar events primary \
  --from "${TODAY}T00:00:00-06:00" \
  --to "${TODAY}T23:59:59-06:00" \
  --account "$ANDRE_ACCOUNT" 2>/dev/null)

CAL_DISPLAY=$(echo "$RAW_CAL" | python3 -c "
import sys, re

def to12(time24):
    parts = time24.split(':')
    h = int(parts[0])
    m = parts[1] if len(parts) > 1 else '00'
    suffix = 'AM' if h < 12 else 'PM'
    h12 = h if h <= 12 else h - 12
    if h12 == 0: h12 = 12
    return str(h12) + ':' + m + ' ' + suffix

for line in sys.stdin.read().splitlines():
    line = line.strip()
    if not line or line.startswith('ID') or line.startswith('#'):
        continue
    m = re.match(r'\S+\s+(\S+)\s+(\S+)\s+(.*)', line)
    if m:
        start, end, summary = m.group(1), m.group(2), m.group(3)
        if 'T' in start:
            time_start = start.split('T')[1][:5]
            time_end = end.split('T')[1][:5] if 'T' in end else ''
            print(to12(time_start) + ' - ' + to12(time_end))
            print('  ' + summary)
        else:
            print('All day')
            print('  ' + summary)
" 2>/dev/null || echo "No events")

# --- TODAY'S GOALS (from goals file set by morning brief, or fallback to Todoist) ---
if [ -f "$GOALS_FILE" ]; then
  GOALS=$(cat "$GOALS_FILE" 2>/dev/null)
else
  # Fallback: pull from Todoist high-priority tasks
  TODOIST_TOKEN="5f09a247ab78d478ae31a9538c08051769bd3cc0"
  GOALS=$(curl -s "https://api.todoist.com/api/v1/tasks?filter=today" \
    -H "Authorization: Bearer $TODOIST_TOKEN" 2>/dev/null | python3 -c "
import sys,json,re
d=json.load(sys.stdin)
tasks = d.get('results', d) if isinstance(d, dict) else d
skip_pattern = re.compile(r'All about tasks|Get Todoist|Viewing tasks|Tip:|Clarify:|Set aside|Completely check|Organize with|Add sections|Discover layouts|Create filtered')
high = [t['content'][:90] for t in tasks if t.get('priority',1) >= 3 and not skip_pattern.search(t['content'])]
if high:
    for c in high[:3]:
        print('- ' + c)
else:
    print('- [No priority tasks set today]')
" 2>/dev/null || echo "- [Could not load tasks]")
fi

# --- BUILD MESSAGE ---
CAL_BLOCK="${CAL_DISPLAY:-No events today}"
GOALS_BLOCK="${GOALS:-No goals set for today}"

BRIEF="🌙 End of Day Review — ${TODAY_CT}

━━━━━━━━━━━━━━━━━

Before you record, review what happened today:

📅 EVENTS TODAY
${CAL_BLOCK}

🎯 GOALS FOR TODAY
${GOALS_BLOCK}

━━━━━━━━━━━━━━━━━

Now record your evening executive review:

1. What did you complete today?
   (Go through each goal and mark it done or not)

2. Where did you fall short?
   (Be honest — what stopped you?)

3. Why did you fall short?
   (Root cause — distraction, energy, priorities?)

4. What are 2-3 priorities for tomorrow?
   (These go into tomorrow's morning briefing)

━━━━━━━━━━━━━━━━━

When done, send me the Fathom link to your recording.
I'll have R2 process it and update your profile.

Good work today, Andre."
echo "$BRIEF"

# --- SEND ---
curl -s -X POST "${TELEGRAM_API}/sendMessage" \
  -d "chat_id=${CHAT_ID}" \
  -d "text=${BRIEF}" \
  -d "disable_notification=false" > /dev/null 2>&1

echo "[$(date)] EOD review sent"
