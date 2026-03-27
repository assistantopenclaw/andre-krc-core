# HEARTBEAT.md — Transcript Scraper (production)

No scheduled heartbeat by default. Production is event-driven through the single clone-lane runner.

On a production URL intake:
1) Validate allowed domain (`fathom` unless allowlist configured)
2) If the URL came from the active one-link processor or queued links file, treat it as an explicit work order and continue even if similar source material was processed before
3) Retrieve transcript through the Fathom API only
4) Write raw transcript, manifest, and run log under `/home/openclaw_agent_1/krc_vault_clone/`
5) Write the nugget export under `/home/openclaw_agent_1/krc_vault_clone/gold nugget exports/`
6) Verify export is non-placeholder and readable
7) Handoff only to `contentwriter`
8) Return compact run status only

On failure:
- write failed manifest state + run log
- escalate to Tommy only with RUN_ID + step + error + log path

Strict isolation:
- never touch `~/krc_vault`
- never hand off to legacy `jimmy`
- no curl fallback
- no scrape fallback
