# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.

Last core-sync review: 2026-02-25T23:35:14-06:00


### Idea Memory Storage
- OPEN ideas: `/home/openclaw_agent_1/.openclaw/workspace-tasklist/ideas/open/*.json`
- ARCHIVE ideas: `/home/openclaw_agent_1/.openclaw/workspace-tasklist/ideas/archive/*.json`
- Manager script: `/home/openclaw_agent_1/.openclaw/workspace-tasklist/scripts/ideas_cli.py`
