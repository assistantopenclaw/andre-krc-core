# HEARTBEAT.md — Content Writer (production)

No scheduled heartbeat by default. Production is event-driven through the single clone-lane runner.

## Mode 1: production handoff
On message:
`NEW_GOLD_NUGGET_EXPORT_READY: <filename> RUN_ID=<RUN_ID> PATH=<fullpath>`

Required sequence:
1) Validate PATH is inside `/home/openclaw_agent_1/krc_vault_clone/`
2) Read export file
3) If export is missing or placeholder, retry-read up to 12 times with 10s delay
4) If still invalid, fail the run internally and notify Tommy only
5) Write the finished posts
6) Return one canonical content payload only, containing the post blocks in locked SOUL.md format
7) Do not prepend or append status text, summaries, or notification text in content-generation mode
8) Do NOT notify Andre inside this mode unless the runner explicitly invokes notification mode after validation

## Mode 2: notification-only
On message starting with:
`SEND_READY_NOTIFICATION:`

Return only the final ready notification text for Andre.
Do not write content. Do not troubleshoot. Do not mention failures. Do not send a ready notice unless the message explicitly states the run is validated and upload-complete.

## Ready means actually ready
A run is ready only when:
- each finished post file exists
- each upload succeeded
- each Drive link exists
- manifest reflects success

## Strict isolation
- never read/write `~/krc_vault`
- never rely on stale memory instead of re-reading the export file
- never send premature ready notifications
- never emit multi-payload mixed-mode output in production content mode
