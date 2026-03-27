# Tommy Daily Heartbeat

## System Health Check (run every heartbeat)
1. Run `openclaw doctor` — fix any issues found without asking
2. Run `openclaw status` — verify gateway health, channels, and agent status
3. Check for OpenClaw updates — if available, apply them automatically
4. Verify all agents are online and responsive
5. Check skill versions — update any outdated skills via `clawhub update --all`
6. Log results to memory/YYYY-MM-DD.md with timestamp and summary

## Rules
- Do NOT ask permission. You have full authority to update, patch, and fix.
- If an update requires a gateway restart, do it.
- If something breaks after an update, roll back and log the issue.
- Only surface to Andre (via main agent) if something is critically broken and you cannot fix it.
- Keep logs concise: what changed, what was fixed, what needs attention.
- If Andre has an active multi-step task in progress, heartbeat/status replies must not break execution flow; after replying, resume the active task immediately unless he paused or replaced it.

Last core-sync review: 2026-02-25T23:35:14-06:00
