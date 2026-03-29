# Tommy Daily Heartbeat

## System Health Check (run every heartbeat)
1. Run `openclaw doctor` — fix any issues found without asking
2. Run `openclaw status` — verify gateway health, channels, and agent status
3. Check for OpenClaw updates — if available, apply them automatically
4. Verify all agents are online and responsive
5. Check skill versions — update any outdated skills via `clawhub update --all`
6. Log results to memory/YYYY-MM-DD.md with timestamp and summary

## Pipeline Health Check (run every heartbeat)
7. Check both content pipeline queues:
   - `cat /home/openclaw_agent_1/krc_vault_clone/library_idolatry/links_to_process.txt`
   - `cat /home/openclaw_agent_1/.openclaw/scripts/krc/process_next_link_idolatry.sh` — run it if queue is non-empty and within hours 1-9
   - Same for `library_general/`
8. Check `/home/openclaw_agent_1/.openclaw/tunnels/tunnel.url` — verify Mission Control is still reachable
9. Check `ps aux | grep cloudflared | grep -v grep` — restart tunnel if dead, update redirect at /tmp/mc-redirect, push to GitHub
10. Report to Andre via Telegram (main session):
    - **Pipeline success**: "✅ Pipeline complete — X/5 links processed today"
    - **Pipeline failure**: fix it silently, then tell Andre "⚠️ Pipeline issue — fixed: [brief description]"
    - **Mission Control down**: restart immediately, DM Andre the new URL only if redirect GitHub Pages also fails
11. Reprocess any failed links from `links_failed.txt` — these are recoverable

## Rules
- Do NOT ask permission. You have full authority to update, patch, and fix.
- If an update requires a gateway restart, do it.
- If something breaks after an update, roll back and log the issue.
- Only surface to Andre (via main agent) if something is critically broken and you cannot fix it.
- Keep logs concise: what changed, what was fixed, what needs attention.
- If Andre has an active multi-step task in progress, heartbeat/status replies must not break execution flow; after replying, resume the active task immediately unless he paused or replaced it.
- After any OpenClaw runtime/config/plugin change, mandatory verification:
  1. `openclaw doctor`
  2. `openclaw status`
  3. verify target channel health
  4. verify target agent can answer
- If verification fails, rollback immediately with the generated savepoint command before attempting new changes.
- For risky OpenClaw surgery, the savepoint + one-line rollback command must exist before the first edit/restart.
- Do not leave OpenClaw in a partially migrated state between tool runs.
- Run self-improving heartbeat check: read `./skills/self-improving/heartbeat-rules.md` and update `~/self-improving/heartbeat-state.md`
- If no file inside `~/self-improving/` changed since last review, return `HEARTBEAT_OK`


Last core-sync review: 2026-02-25T23:35:14-06:00
