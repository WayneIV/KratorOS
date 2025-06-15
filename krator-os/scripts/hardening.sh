#!/bin/bash
# System hardening script for Krator OS
set -e

# Enable UFW firewall
if command -v ufw >/dev/null; then
    ufw --force enable
    ufw default deny incoming
    ufw default allow outgoing
fi

# Install and configure fail2ban
if ! command -v fail2ban-client >/dev/null; then
    apt-get update && apt-get install -y fail2ban
fi
systemctl enable --now fail2ban.service

# Ensure auditd is installed
if ! command -v auditctl >/dev/null; then
    apt-get update && apt-get install -y auditd
fi
systemctl enable --now auditd.service

echo "Hardening complete"
