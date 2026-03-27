#!/bin/bash
# Two-path voice note transcription router
# Usage: transcribe.sh <audio_file>
# - Under 2 min audio: fast path (tiny.en, faster-whisper, CPU, int8)
# - Over 2 min audio: accuracy path (base model, faster-whisper, CPU)
# Output: transcript text to stdout, file saved to voice_notes_inbox

set -e

AUDIO_FILE="$1"
INBOX_DIR="/home/openclaw_agent_1/.openclaw/workspace/voice_notes_inbox"
VENV="/home/openclaw_agent_1/.venv/fast-whisper"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BASENAME=$(basename "$AUDIO_FILE" | sed 's/\.[^.]*$//')
OUTPUT_FILE="${INBOX_DIR}/transcript_${TIMESTAMP}_${BASENAME}.txt"

if [ -z "$AUDIO_FILE" ] || [ ! -f "$AUDIO_FILE" ]; then
  echo "ERROR: Provide a valid audio file path" >&2
  exit 1
fi

mkdir -p "$INBOX_DIR"

source "$VENV/bin/activate"

python3 -c "
import sys, time, json

audio_path = '$AUDIO_FILE'
output_path = '$OUTPUT_FILE'
timestamp = '$TIMESTAMP'

from faster_whisper import WhisperModel

# First pass: get duration via VAD/segments with tiny.en (fast)
start = time.time()
fast_model = WhisperModel('tiny.en', device='cpu', compute_type='int8')
segments_list = []
segments, info = fast_model.transcribe(audio_path, language='en', beam_size=1, vad_filter=True)
for s in segments:
    segments_list.append({'start': s.start, 'end': s.end, 'text': s.text.strip()})

duration = segments_list[-1]['end'] if segments_list else 0
fast_text = ' '.join([s['text'] for s in segments_list])
fast_time = time.time() - start

# Decide path
if duration > 120:
    # Accuracy path: re-transcribe with base model
    start2 = time.time()
    acc_model = WhisperModel('base', device='cpu', compute_type='int8')
    acc_segments, acc_info = acc_model.transcribe(audio_path, language='en', beam_size=5, vad_filter=True)
    acc_text = ' '.join([s.text.strip() for s in acc_segments])
    acc_time = time.time() - start2
    final_text = acc_text
    path_used = 'accuracy (base, beam=5)'
    total_time = fast_time + acc_time
else:
    final_text = fast_text
    path_used = 'fast (tiny.en, beam=1)'
    total_time = fast_time

# Write transcript file
with open(output_path, 'w') as f:
    f.write(final_text)

# Write metadata sidecar
meta = {
    'timestamp': timestamp,
    'audio_file': audio_path,
    'duration_seconds': round(duration, 2),
    'path_used': path_used,
    'transcription_time_seconds': round(total_time, 2),
    'transcript_file': output_path
}
meta_path = output_path.replace('.txt', '_meta.json')
with open(meta_path, 'w') as f:
    json.dump(meta, f, indent=2)

# Output to stdout
print(final_text)
print(f'---', file=sys.stderr)
print(f'PATH: {path_used}', file=sys.stderr)
print(f'DURATION: {duration:.1f}s', file=sys.stderr)
print(f'TRANSCRIPTION TIME: {total_time:.2f}s', file=sys.stderr)
print(f'SAVED: {output_path}', file=sys.stderr)
"
