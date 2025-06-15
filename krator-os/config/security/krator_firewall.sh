#!/bin/bash
# Dynamic firewall setup using UFW
set -e

LOG=/var/log/krator_firewall.log
exec >> "$LOG" 2>&1

echo "[firewall] configuring UFW" $(date)

if ! command -v ufw >/dev/null; then
    apt-get update && apt-get install -y ufw
fi

ufw --force reset
ufw default deny incoming
ufw default allow outgoing

# Allow SSH
ufw allow 22/tcp

ufw --force enable

echo "[firewall] rules applied" $(date)
