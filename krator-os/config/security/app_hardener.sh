#!/bin/bash
# Remove unnecessary packages and disable telemetry services
set -e

LOG=/var/log/app_hardener.log
exec >> "$LOG" 2>&1

echo "[hardener] removing bloat" $(date)

UNNEEDED_PACKAGES=(popularity-contest apport)
apt-get purge -y "${UNNEEDED_PACKAGES[@]}" || true
apt-get autoremove -y

# Disable telemetry services if present
systemctl disable --now whoopsie.service 2>/dev/null || true
systemctl disable --now apport.service 2>/dev/null || true

echo "[hardener] complete" $(date)
