import json
import sys

with open("transcript_raw.json", "r") as f:
    data = json.load(f)
    chunks = data.get("transcript") or []
    for c in chunks:
        ts = c.get("timestamp", "")
        name = (c.get("speaker") or {}).get("display_name", "Unknown")
        text = c.get("text", "")
        print(f"[{ts}] {name}: {text}")
