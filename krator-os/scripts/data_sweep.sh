#!/bin/bash
# Collect basic system info and perform OSINT queries via curl
set -e

LOG=/var/log/data_sweep.log
exec >> "$LOG" 2>&1

echo "[sweep] gathering system data" $(date)

uname -a
ip addr show

if command -v curl >/dev/null; then
    curl -s https://ipinfo.io
fi
