# KRC Marketing Pipeline Scaffold (Donald -> Jimmy)

This scaffold creates the filesystem layout + helper scripts for the Donald (Extractor) -> Jimmy (Content Creator) pipeline.

Important: Donald/Jimmy *business logic* (transcript parsing, nugget scoring, caption format, hooks) must be provided by Andre via SOUL/IDENTITY in the Gateway dashboard.

Vault root: `~/krc_vault/`

Folders (must match exactly):
- `raw call transcripts/`
- `gold nugget exports/`
- `finished content for posting/`
- `run logs/`
- `manifests/`

Scripts (installed by Tommy into `~/.openclaw/scripts/krc/`):
- `run_helpers.py`
- `donald_process_url.py` (uses curl, no python requests dependency)
- `jimmy_process_export.py`

Smoke test approach:
1) Donald script writes raw transcript + placeholder nugget export + manifest
2) Jimmy script writes placeholder finished content + updates manifest
3) Drive upload requires `gog auth` first
