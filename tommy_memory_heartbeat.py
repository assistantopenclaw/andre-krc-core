#!/usr/bin/env python3
"""
Tommy Auto-Memory Heartbeat
Fires every 15 min. Detects new Andre messages → summarizes via MiniMax API → writes to memory.
"""
import json, os, subprocess, datetime, re, urllib.request
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────
SESSIONS_JSON = Path.home() / ".openclaw/agents/tommy/sessions/sessions.json"
STATE_FILE    = Path.home() / ".openclaw/tommy_memory_last_msg.txt"
MEMORY_DIR    = Path.home() / ".openclaw/workspace-tommy/memory"
OPENROUTER_KEY = "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"
MODEL_ID      = "google/gemini-3-flash-preview"
# ─────────────────────────────────────────────────────────────────────────────

def log(msg):
    print(f"[tommy-memory-beat] {msg}", flush=True)

def get_active_session():
    with open(SESSIONS_JSON) as f:
        data = json.load(f)
    for key in ["agent:tommy:telegram:direct:8434682557"]:
        entry = data.get(key)
        if entry:
            sf = entry.get("sessionFile")
            if sf and Path(sf).exists():
                return Path(sf)
    return None

def count_lines(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return sum(1 for line in f if line.strip())
    except:
        return 0

def extract_user_messages(path, since_line, limit=20):
    """Extract Andre's messages since checkpoint. Returns list of (ts_str, text)."""
    results = []
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            all_lines = [l.strip() for l in f if l.strip()]
    except Exception as e:
        log(f"Error reading session: {e}")
        return results

    recent = all_lines[since_line:]
    if not recent:
        return results

    for raw in recent:
        try:
            d = json.loads(raw)
            msg = d.get("message", {})
            if msg.get("role") != "user":
                continue
            content = msg.get("content", [])
            text_parts = []
            if isinstance(content, list):
                for c in content:
                    if isinstance(c, dict) and c.get("type") == "text":
                        raw_text = c.get("text", "")
                        cleaned = _strip_metadata(raw_text)
                        if cleaned.strip():
                            text_parts.append(cleaned)
            if text_parts:
                ts = msg.get("timestamp", "")
                try:
                    if ts:
                        dt = datetime.datetime.fromisoformat(str(ts).replace("Z", "+00:00"))
                        ts_str = dt.strftime("%H:%M")
                    else:
                        ts_str = "??"
                except:
                    ts_str = "??"
                results.append((ts_str, " ".join(text_parts)))
        except Exception:
            pass
    return results[-limit:]  # Most recent N for prompt

def _strip_metadata(text):
    """Strip OpenClaw Telegram metadata headers."""
    text = re.sub(r"Conversation info \(untrusted metadata\):\s*\n\`\`\`.*?\n\`\`\`", "", text, flags=re.DOTALL)
    text = re.sub(r"Sender \(untrusted metadata\):\s*\n\`\`\`.*?\n\`\`\`", "", text, flags=re.DOTALL)
    return text.strip()

def call_minimax(prompt, max_tokens=300):
    """Call MiniMax M2.7 via OpenRouter API. Returns response text or None."""
    body = {
        "model": MODEL_ID,
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": max_tokens,
        "temperature": 0.3,
    }
    req = urllib.request.Request(
        "https://openrouter.ai/api/v1/chat/completions",
        data=json.dumps(body).encode(),
        headers={
            "Authorization": f"Bearer {OPENROUTER_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "https://openclaw.ai",
            "X-Title": "Tommy-AutoMemory",
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode())
            choices = data.get("choices", [])
            if choices:
                return choices[0].get("message", {}).get("content", "").strip()
    except Exception as e:
        log(f"API error: {e}")
    return None

def build_prompt(user_messages, today_str):
    msg_lines = []
    for ts, text in user_messages[-15:]:  # Last 15 messages
        truncated = text[:250] + "..." if len(text) > 250 else text
        msg_lines.append(f"[{ts}] Andre: {truncated}")
    messages_block = "\n".join(msg_lines) or "(no Andre messages)"

    return f"""You are tommy, Andre Panet-Raymond's executive assistant (coding/growth/IT).

Write a memory entry based on today's Telegram conversation with Andre.

DATE: {today_str}

ANDRE MESSAGES (oldest → newest):
{messages_block}

Write a concise memory block to append to the memory file. Format:
## {today_str} — Session Summary

- [key decision or action taken]
- [something that changed or broke]
- [preference or pattern Andre expressed]
- [unresolved item or follow-up needed]
- [anything to carry into next session]

Rules:
- Write ONLY the memory block above — nothing else
- Be factual; do not invent details
- If Andre only sent short acknowledgements, write minimal bullets
- 3-6 bullets max
- Do not include any markdown code fences
"""

def write_memory_block(output, memory_file, today_str):
    """Write the memory block to the memory file."""
    # Skip if already has today's entry
    existing = memory_file.read_text() if memory_file.exists() else ""
    marker = f"## {today_str} — Session Summary"
    if marker in existing:
        log("Today's entry already exists — skipping")
        return False
    # Clean the output (remove any fences)
    output = re.sub(r"^```.*$", "", output, flags=re.MULTILINE).strip()
    if len(output) < 30:
        log(f"Output too short ({len(output)} chars) — skipping")
        return False
    memory_file.write_text(existing.rstrip() + "\n\n" + output + "\n")
    log(f"Memory written ({len(output)} chars) to {memory_file.name}")
    return True

def main():
    log("Heartbeat fired")
    session_file = get_active_session()
    if not session_file:
        log("No active session — exiting")
        sys.exit(0)

    current_lines = count_lines(session_file)
    last_checkpoint = int(STATE_FILE.read_text().strip()) if STATE_FILE.exists() else 0

    if current_lines <= last_checkpoint:
        log(f"No new activity ({last_checkpoint} → {current_lines}) — exiting")
        sys.exit(0)

    log(f"New activity: lines {last_checkpoint} → {current_lines}")

    user_msgs = extract_user_messages(session_file, last_checkpoint)
    log(f"Andre messages since checkpoint: {len(user_msgs)}")

    if len(user_msgs) < 2:
        log("Fewer than 2 Andre messages — skipping")
        STATE_FILE.write_text(str(current_lines))
        sys.exit(0)

    today_str = datetime.date.today().strftime("%Y-%m-%d")
    memory_file = MEMORY_DIR / f"{today_str}.md"
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)

    prompt = build_prompt(user_msgs, today_str)
    output = call_minimax(prompt)

    if output:
        write_memory_block(output, memory_file, today_str)
    else:
        log("Summarizer failed — skipping")

    STATE_FILE.write_text(str(current_lines))
    log(f"Checkpoint saved: line {current_lines}")

if __name__ == "__main__":
    import sys
    main()
