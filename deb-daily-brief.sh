#!/bin/bash
# Daily Executive Briefing - Andre's KRC PA
# Runs via Manager agent cron at 7am CT daily

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
MEMORY_PATH="/home/openclaw_agent_1/.openclaw/workspace-tommy/memory/${YESTERDAY}.md"

# --- WEATHER (current + low + high in Fahrenheit) ---
WEATHER=$(curl -s "https://wttr.in/Chicago?format=j1" 2>/dev/null | python3 -c "
import sys,json
d=json.load(sys.stdin)
w = d['weather'][0]
cur = d['current_condition'][0]
print('Current: ' + cur['temp_F'].strip() + 'F, ' + cur['weatherDesc'][0]['value'])
print('Low: ' + w['mintempF'].strip() + 'F  |  High: ' + w['maxtempF'].strip() + 'F')
" 2>/dev/null || echo "Weather unavailable")

# --- CALENDAR (today, 12-hour time, human-readable) ---
RAW_CAL=$(GOG_KEYRING_BACKEND=file GOG_KEYRING_PASSWORD="$GOG_KEYRING_PASSWORD" \
  gog calendar events primary \
  --from "${TODAY}T00:00:00-06:00" \
  --to "${TODAY}T23:59:59-06:00" \
  --account "$ANDRE_ACCOUNT" 2>/dev/null)

CAL_FORMATTED=$(echo "$RAW_CAL" | python3 -c "
import sys, re

def to12(time24):
    # time24 format: HH:MM
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
    else:
        print(line)
" 2>/dev/null || echo "No events")

# --- TODOIST (filter tutorial/brain dump tasks) ---
TODOIST_TOKEN="5f09a247ab78d478ae31a9538c08051769bd3cc0"

FILTERED_TASKS=$(curl -s "https://api.todoist.com/api/v1/tasks?filter=today|overdue" \
  -H "Authorization: Bearer $TODOIST_TOKEN" 2>/dev/null | python3 -c "
import sys,json,re
d=json.load(sys.stdin)
tasks = d.get('results', d) if isinstance(d, dict) else d
skip_pattern = re.compile(r'All about tasks|Get Todoist|Viewing tasks|Tip:|Clarify:|Set aside|Completely check|Organize with|Add sections|Discover layouts|Create filtered')
high = [(t['content'][:200], t.get('priority',1)) for t in tasks 
        if t.get('priority',1) >= 3 and not skip_pattern.search(t['content'])]
if not high:
    print('None')
else:
    first = True
    for i, (c, p) in enumerate(high[:4], 1):
        if not first:
            print('')
        first = False
        print(str(i) + '. ' + c)
" 2>/dev/null || echo "None")

OVERDUE_TASKS=$(curl -s "https://api.todoist.com/api/v1/tasks?filter=overdue" \
  -H "Authorization: Bearer $TODOIST_TOKEN" 2>/dev/null | python3 -c "
import sys,json,re
d=json.load(sys.stdin)
tasks = d.get('results', d) if isinstance(d, dict) else d
skip_pattern = re.compile(r'All about tasks|Get Todoist|Viewing tasks|Tip:|Clarify:|Set aside|Completely check|Organize with|Add sections|Discover layouts|Create filtered')
overdue = [t['content'][:90] for t in tasks if not skip_pattern.search(t['content'])]
if overdue:
    first = True
    for t in overdue[:3]:
        if not first:
            print('')
        first = False
        print('  Overdue: ' + t)
" 2>/dev/null)

# --- CONTENT PIPELINE ---
IDOLATRY_COUNT=""
GENERAL_COUNT=""
if [ -f "/home/openclaw_agent_1/krc_vault_clone/library_idolatry/links_completed.txt" ]; then
  IDOLATRY_COUNT=$(wc -l < /home/openclaw_agent_1/krc_vault_clone/library_idolatry/links_completed.txt 2>/dev/null || echo "")
fi
if [ -f "/home/openclaw_agent_1/krc_vault_clone/library_general/links_completed.txt" ]; then
  GENERAL_COUNT=$(wc -l < /home/openclaw_agent_1/krc_vault_clone/library_general/links_completed.txt 2>/dev/null || echo "")
fi

# --- YESTERDAY'S MEMORY (human summary) ---
if [ -f "$MEMORY_PATH" ]; then
  YESTERDAY_MEM=$(python3 -c "
import re
path = '/home/openclaw_agent_1/.openclaw/workspace-tommy/memory/${YESTERDAY}.md'
text = open(path).read()
entries = re.split(r'(?m)^- \d{2}:\d{2}', text)
parts = []
for entry in entries[1:]:
    lines = [l.strip() for l in entry.splitlines() 
             if l.strip() and not l.startswith('#') and 'core-sync' not in l
             and not re.search(r'/[a-zA-Z0-9_.-]{20,}', l)]
    if lines:
        text_block = ' '.join(lines)[:120]
        if text_block:
            parts.append(text_block)
print('  '.join(parts[:6]))
" 2>/dev/null || echo "")
else
  YESTERDAY_MEM=""
fi

# --- BUILD BRIEF ---
CAL_DISPLAY="${CAL_FORMATTED:-No events scheduled}"
TASKS_DISPLAY="${FILTERED_TASKS:-None}"
OVERDUE_DISPLAY="${OVERDUE_TASKS:-}"
CONTENT_DISPLAY=""
if [ -n "$IDOLATRY_COUNT" ] || [ -n "$GENERAL_COUNT" ]; then
  CONTENT_DISPLAY="${IDOLATRY_COUNT:+Idolatry: ${IDOLATRY_COUNT} links completed this week
}${GENERAL_COUNT:+General: ${GENERAL_COUNT} links completed this week}"
else
  CONTENT_DISPLAY="No content data yet"
fi
MEM_DISPLAY="${YESTERDAY_MEM:-No summary available.}"

BRIEF="🌅 Good Morning, Andre — ${TODAY_CT}

━━━━━━━━━━━━━━━━━

🌤️ WEATHER — Chicago

${WEATHER}

━━━━━━━━━━━━━━━━━

📅 TODAY'S SCHEDULE

${CAL_DISPLAY}

━━━━━━━━━━━━━━━━━

🎯 PRIORITY TASKS

${TASKS_DISPLAY}
${OVERDUE_DISPLAY}

━━━━━━━━━━━━━━━━━

🎬 CONTENT PIPELINE

${CONTENT_DISPLAY}

━━━━━━━━━━━━━━━━━

📊 YESTERDAY

${MEM_DISPLAY}"

# --- SAVE GOALS FOR EOD REVIEW ---
GOALS_FILE="/tmp/eod_goals_${TODAY}.txt"
if [ -n "$FILTERED_TASKS" ] && [ "$FILTERED_TASKS" != "None" ]; then
  echo "$FILTERED_TASKS" > "$GOALS_FILE"
fi

# --- SEND ---
curl -s -X POST "${TELEGRAM_API}/sendMessage" \
  -d "chat_id=${CHAT_ID}" \
  -d "text=${BRIEF}" \
  -d "disable_notification=false" > /dev/null 2>&1

echo "Briefing sent at $(date)"
