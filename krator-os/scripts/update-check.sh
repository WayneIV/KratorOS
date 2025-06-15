#!/bin/bash
# Check for OS and Krator updates
set -e

LOG=/var/log/update_check.log
exec >> "$LOG" 2>&1

echo "[update] checking for updates" $(date)

apt-get update
apt-get --just-print upgrade

if python3 -m krator.agents.assistant --version >/dev/null 2>&1; then
    echo "Krator daemon present"
fi
