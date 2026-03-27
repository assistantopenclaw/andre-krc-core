# BOOTSTRAP.md — Jimmy (Clone Lane)

Uses clone vault only: `~/krc_vault_clone/`

Ensure folders exist:
- `gold nugget exports`
- `finished content for posting`
- `manifests`
- `run logs`
- `queue`
- `google_drive_exports`

Strict separation:
- Never read/write `~/krc_vault/`
- Always run with `KRC_VAULT_ROOT=/home/openclaw_agent_1/krc_vault_clone`
- Writer target is this agent (`contentwriter`) only
