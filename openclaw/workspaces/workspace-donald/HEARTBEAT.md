# HEARTBEAT.md - Donald

No scheduled heartbeat by default. Event-driven only.

On message containing a Fathom URL:
1) Return one line immediately:
   `Received. Processing now. RUN_ID=<RUN_ID>.`
2) Run full deterministic 5-agent pipeline end-to-end with that URL:
   `python3 /home/openclaw_agent_1/.openclaw/scripts/krc/deterministic_pipeline_v2.py --url "<URL>"`
3) Do not stop at Donald-only extraction.

On success:
- Final output must land in Google Drive doc via Jimmy stage.

On failure:
- Return one line:
  `Couldn’t process automatically. Tommy has been alerted. RUN_ID=<RUN_ID>.`
- Log error in manifest and run log only.

Never leak payloads or file paths in user chat.
