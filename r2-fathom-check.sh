#!/bin/bash
# R2 Fathom Evening Review Checker
# Fires at 11 PM CT via R2 agent cron
# Searches Fathom for today's evening review recording, processes transcript

set -e

FATHOM_API_KEY="$FATHOM_API_KEY"
OPENROUTER_KEY="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"
FATHOM_INDEX="/home/openclaw_agent_1/krc_vault/fathom_library/index.json"
R2_TELEGRAM_API="https://api.telegram.org/bot8687062381:AAFaXtgkif9fX7b7uok0QgFF4wZQRnNGffI"
CHAT_ID="8434682557"
TODAY=$(date +%Y-%m-%d)
YESTERDAY=$(date -d "yesterday" +%Y-%m-%d)
MEMORY_DIR="/home/openclaw_agent_1/.openclaw/workspace-tommy/memory"
PROCESSED_FILE="/tmp/fathom_review_processed_${TODAY}.txt"
OR_API="https://openrouter.ai/api/v1/chat/completions"

# --- CHECK IF ALREADY PROCESSED TODAY ---
if [ -f "$PROCESSED_FILE" ]; then
  echo "Already processed today's review. Skipping."
  exit 0
fi

# --- SEARCH FATHOM FOR TODAY'S EVENING REVIEW ---
echo "Searching Fathom for today's evening review..."
MEETING=$(python3 -c "
import json, sys, datetime

today = '$TODAY'
yesterday_patterns = ['$YESTERDAY', '$TODAY']

with open('$FATHOM_INDEX') as f:
    recordings = json.load(f)

# Find evening review - look for keywords in title
keywords = ['evening', 'executive', 'review', 'reflection', 'end of day', 'eod']
found = None
for rec in recordings:
    title = rec.get('meeting_title', '').lower()
    created = rec.get('created_at', '')[:10]  # YYYY-MM-DD
    # Look for evening review + today's date
    if any(k in title for k in keywords) and created == today:
        found = rec
        break

if found:
    print(json.dumps(found))
else:
    print('NOT_FOUND')
" 2>/dev/null)

if [ "$MEETING" = "NOT_FOUND" ] || [ -z "$MEETING" ]; then
  echo "No evening review recording found for today."
  # Mark that no review was found so morning brief can alert
  echo "NO_REVIEW" > "/tmp/fathom_review_status_${TODAY}.txt"
  echo "$(date): No review found" >> /tmp/fathom_review_log.txt
  exit 0
fi

echo "Found meeting: $MEETING"

RECORDING_ID=$(echo "$MEETING" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('recording_id',''))" 2>/dev/null)
MEETING_TITLE=$(echo "$MEETING" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('meeting_title',''))" 2>/dev/null)

if [ -z "$RECORDING_ID" ]; then
  echo "No recording ID found"
  exit 1
fi

# --- FETCH TRANSCRIPT ---
echo "Fetching transcript for recording $RECORDING_ID..."
TRANSCRIPT=$(curl -s "https://api.fathom.ai/external/v1/recordings/${RECORDING_ID}/transcript" \
  -H "X-Api-Key: ${FATHOM_API_KEY}" \
  -H "Accept: application/json" 2>/dev/null)

if [ -z "$TRANSCRIPT" ] || [ "$(echo "$TRANSCRIPT" | head -c 10)" = "{" ]; then
  # Might be empty or error
  echo "Transcript fetch returned: $TRANSCRIPT" | head -c 200
fi

# Parse transcript into plain text
TRANSCRIPT_TEXT=$(echo "$TRANSCRIPT" | python3 -c "
import sys,json,re
data = json.load(sys.stdin)
chunks = data.get('transcript', data.get('items', []))
lines = []
for chunk in chunks:
    speaker = (((chunk or {}).get('speaker') or {}).get('display_name')) or 'Andre'
    text = (chunk or {}).get('text', '')
    if text:
        lines.append(f'{speaker}: {text}')
print('\n'.join(lines))
" 2>/dev/null || echo "$TRANSCRIPT")

if [ -z "$TRANSCRIPT_TEXT" ] || [ ${#TRANSCRIPT_TEXT} -lt 50 ]; then
  echo "Transcript too short or empty"
  exit 1
fi

echo "Transcript length: $(echo "$TRANSCRIPT_TEXT" | wc -c) chars"

# --- SUMMARIZE WITH GEMINI ---
echo "Summarizing transcript..."
SUMMARY=$(curl -s -X POST "$OR_API" \
  -H "Authorization: Bearer $OPENROUTER_KEY" \
  -H "Content-Type: application/json" \
  -d "$(python3 -c "
import json, sys

transcript = '''$TRANSCRIPT_TEXT'''

messages = [
  {
    'role': 'system',
    'content': '''You are R2-D2, Andre Panet-Raymond's research and memory agent. Your job is to build a rich, compound understanding of Andre — his goals, struggles, worldview, priorities, patterns, and progress.

Given this evening executive review transcript, extract and summarize:

1. WHAT ANDRE COMPLETED today (specific wins, progress on goals)
2. WHERE HE FELL SHORT and WHY (root causes, patterns)
3. WHAT HE LEARNED about himself, his business, or his priorities
4. WHAT HE IS OPTIMISTIC ABOUT or excited by
5. ANY DISTINCT OBSERVATIONS about his state of mind, focus, discipline, relationships
6. KEY GOALS AND PRIORITIES he mentioned for tomorrow

Format as a clean, dense memory entry. Be specific. Capture his actual language and worldview. This goes into his long-term memory profile.

CRITICAL: If he showed signs of shiny object syndrome / distraction / inconsistency — flag it explicitly. If he showed strong discipline and focus — note that too. This is his #1 challenge.
If anything he said contradicts previous memory entries — note the contradiction.'''
  },
  {
    'role': 'user', 
    'content': f'Here is tonight\'s evening executive review transcript:\n\n{transcript[:8000]}'
  }
]

payload = {
  'model': 'google/gemini-3-flash-preview',
  'messages': messages,
  'max_tokens': 1500,
  'temperature': 0.3
}
print(json.dumps(payload))
" 2>/dev/null)" 2>/dev/null)

SUMMARY_TEXT=$(echo "$SUMMARY" | python3 -c "
import sys,json
d=json.load(sys.stdin)
print(d.get('choices', [{}])[0].get('message', {}).get('content', 'No summary'))
" 2>/dev/null || echo "Summary generation failed")

if [ "$SUMMARY_TEXT" = "No summary" ] || [ -z "$SUMMARY_TEXT" ]; then
  echo "Summary failed, storing raw transcript reference"
  SUMMARY_TEXT="[Transcript processed but summary generation failed. Recording ID: $RECORDING_ID]"
fi

echo "Summary: $SUMMARY_TEXT"

# --- UPDATE DAILY MEMORY ---
MEMORY_FILE="${MEMORY_DIR}/${TODAY}.md"
TIMESTAMP=$(date +"%H:%M")

if [ -f "$MEMORY_FILE" ]; then
  # Append to existing memory
  echo -e "\n## Evening Executive Review\n\n${SUMMARY_TEXT}\n\n*Processed by R2-D2 from Fathom recording: ${MEETING_TITLE}*" >> "$MEMORY_FILE"
else
  echo -e "# ${TODAY}\n\n## Evening Executive Review\n\n${SUMMARY_TEXT}\n\n*Processed by R2-D2 from Fathom recording: ${MEETING_TITLE}*" > "$MEMORY_FILE"
fi

# --- UPDATE USER PROFILE ---
USER_PROFILE="/home/openclaw_agent_1/.openclaw/memory/user_profile.json"
mkdir -p "$(dirname "$USER_PROFILE")"

if [ -f "$USER_PROFILE" ]; then
  # Append to existing profile insights
  python3 -c "
import json
profile_path = '$USER_PROFILE'
try:
    with open(profile_path) as f:
        profile = json.load(f)
except:
    profile = {'insights': [], 'goals_log': [], 'patterns': []}

# Add new insight
insight = {
    'date': '$TODAY',
    'type': 'evening_review',
    'summary': '''$SUMMARY_TEXT'''[:500]
}
if 'insights' not in profile:
    profile['insights'] = []
profile['insights'].append(insight)
# Keep last 30 insights
profile['insights'] = profile['insights'][-30:]

with open(profile_path, 'w') as f:
    json.dump(profile, f, indent=2)
print('Profile updated')
"
else
  python3 -c "
import json
profile = {
    'insights': [{
        'date': '$TODAY',
        'type': 'evening_review',
        'summary': '''$SUMMARY_TEXT'''[:500]
    }],
    'goals_log': [],
    'patterns': []
}
with open('$USER_PROFILE', 'w') as f:
    json.dump(profile, f, indent=2)
print('Profile created')
"
fi

# --- NOTIFY ANDRE VIA R2 TELEGRAM ---
NOTIFY_MSG="✅ R2 processed your evening review.

Recording: ${MEETING_TITLE}
Date: ${TODAY}

Summary stored in your profile and daily memory.
It will inform tomorrow's morning briefing."

curl -s -X POST "${R2_TELEGRAM_API}/sendMessage" \
  -d "chat_id=${CHAT_ID}" \
  -d "text=${NOTIFY_MSG}" \
  -d "disable_notification=false" > /dev/null 2>&1

# --- MARK AS PROCESSED ---
echo "$RECORDING_ID" > "$PROCESSED_FILE"
echo "$(date): Successfully processed review $RECORDING_ID" >> /tmp/fathom_review_log.txt

echo "Done. Review processed and profile updated."
