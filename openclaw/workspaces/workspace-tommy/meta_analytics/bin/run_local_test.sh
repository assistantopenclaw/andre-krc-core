#!/usr/bin/env bash
set -euo pipefail

# Local test runner (no token committed).
# Usage:
#   export META_SYSTEM_USER_TOKEN='...'
#   export GDRIVE_CONTENT_ANALYTICS_FOLDER_ID='...'
#   bash run_local_test.sh

export TZ="America/Chicago"
export META_GRAPH_VERSION="${META_GRAPH_VERSION:-v19.0}"
export GDRIVE_CONTENT_ANALYTICS_FOLDER_ID="${GDRIVE_CONTENT_ANALYTICS_FOLDER_ID:-17vjnPR3hiwYu5dd0OMQiugZ9IAV-XiGE}"

python3 "$(dirname "$0")/meta_analytics_run.py"
