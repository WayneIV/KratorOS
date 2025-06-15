#!/bin/bash
# Check for OS and Krator updates
set -e

LOG=/var/log/update_check.log
exec >> "$LOG" 2>&1

echo "[update] checking for updates" $(date)

apt-get update
apt-get --just-print upgrade

if [ -f /usr/local/bin/krator_daemon.py ]; then
    echo "Krator daemon version:" $(grep -m1 VERSION /usr/local/bin/krator_daemon.py || true)
fi
