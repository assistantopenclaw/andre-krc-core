# andre-krc-core

Sanitized snapshot of Andre Panet-Raymond's OpenClaw operating system.

## Included
- `openclaw/openclaw.json` with secrets replaced by placeholders
- `openclaw/credentials/` sanitized credential references only
- `openclaw/workspaces/` active agent workspace snapshots
- `agents/` selected agent configs and model/auth profile files
- `scripts/` shared scripts
- `cron/` cron job definitions
- `skills/` installed workspace skill directories

## Security
No live secrets are stored in this repo. Use `.env.example` to populate required environment variables locally.

## Notes
- Historical cron run logs were intentionally excluded.
- This repo is intended for backup, inspection, and controlled edits.
