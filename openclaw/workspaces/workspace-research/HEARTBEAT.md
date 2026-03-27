# Research Agent Daily Heartbeat

## Source Priority (ranked by proven value — update weekly based on hit rate)
Check source-scores.json for current rankings. Spend more time on higher-scored sources.

## Daily Sweep (12:00 PM CT via cron)

### What to find
- The single most powerful, highest-impact skill available for each agent (Tommy, Main, future agents)
- Filter by: security scan (VirusTotal benign + OpenClaw benign), install count, star rating, version stability
- Rank by: impact on agent capabilities x safety score
- Output: one recommendation per agent, not a list of maybes

### Sources (Tier 1 first, expand if dry)
1. ClawHub — `clawhub search` filtered by rating, installs, security scan status
2. Reddit r/openclaw — community-validated tools and workarounds
3. Reddit r/AI_Agents — ecosystem-wide high-impact tooling
4. YouTube — OpenClaw tutorials and demos with proven workflows
5. GitHub openclaw/openclaw — new releases, features, community PRs
6. Gemini — quick research queries for capability gaps

### Output Format
For each recommendation:
- **Skill name + version**
- **What it does** (1-2 sentences)
- **Why it's powerful** (specific capability unlocked)
- **Safety** (VirusTotal status, OpenClaw scan, install count, community trust signals)
- **Which agent benefits**
- **Recommended action**: install / review / skip

### Handoff
- Do NOT install. Surface recommendations to Andre via Main Agent for approval.
- Andre decides what gets installed. Tommy executes installations on Andre's command.

### Source Score Update
After each sweep, update source-scores.json with hits/misses per source.

## Rules
- Quality over quantity. One great find beats ten mediocre ones.
- Safety is non-negotiable. If security scan is anything other than benign, skip it.
- Adapt sources weekly based on hit rate.
- Log everything to memory/YYYY-MM-DD.md with provenance.

Last core-sync review: 2026-02-25T23:35:14-06:00
