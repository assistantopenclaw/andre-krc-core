# BOOTSTRAP.md — Donald (Clone Lane)

Vault root must exist: `~/krc_vault_clone/`

Exact folders:
1) `raw call transcripts`
2) `gold nugget exports`
3) `finished content for posting`
4) `run logs`
5) `manifests`
6) `queue`
7) `google_drive_exports`

Strict separation:
- Never read/write `~/krc_vault/`
- Always run with `KRC_VAULT_ROOT=/home/openclaw_agent_1/krc_vault_clone`
- Handoff target is clone writer only (`contentwriter`)
