# TOOLS.md — Transcript Scraper (production)

Required capabilities:
- Read/write files under `/home/openclaw_agent_1/krc_vault_clone/`
- Fetch transcript text from the Fathom API only
- Internal agent-to-agent messaging / handoff to `contentwriter`
- Internal escalation to Tommy only on failure

Prohibited:
- Any reads/writes to `~/krc_vault` in production
- Telegram DM to Andre
- curl/scrape/browser fallback retrieval
