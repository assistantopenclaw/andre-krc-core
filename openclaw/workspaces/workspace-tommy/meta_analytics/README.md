# Openclaw Content Analytics (Meta)

This package builds the “Content Analysis” reporting system for Andre’s Meta accounts (Facebook Page + Instagram Professional account).

## What it does
- Pulls raw analytics from Meta Graph API (read-only permissions).
- Normalizes/aggregates metrics.
- Generates a Google Doc report.
- Uploads it into the Drive folder: **Openclaw Content Analytics**.
- Intended to run twice daily: **11:00 AM** and **11:00 PM** America/Chicago (via Research agent cron).

## Drive Folder
- Folder name: `Openclaw Content Analytics`
- Folder ID: `17vjnPR3hiwYu5dd0OMQiugZ9IAV-XiGE`

## Configuration (no secrets in repo)
Environment variables:
- `META_SYSTEM_USER_TOKEN` (required)
- `META_GRAPH_VERSION` (optional; default: `v19.0`)
- `META_PAGE_ID` (required after discovery)
- `GDRIVE_CONTENT_ANALYTICS_FOLDER_ID` (required; set to the folder id above)
- `TZ` should be `America/Chicago` for correct report timestamps.

## Files
- `bin/meta_analytics_run.py` — orchestrator.
- `bin/meta_graph_client.py` — thin HTTP client.
- `bin/meta_endpoints.py` — endpoint helpers for FB/IG.

## Safety
- Read-only by design.
- If Meta API auth fails, script exits non-zero and produces an error-only report (no fabricated metrics).
