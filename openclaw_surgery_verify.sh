#!/usr/bin/env bash
set -euo pipefail

openclaw doctor
printf '\n'
openclaw status
