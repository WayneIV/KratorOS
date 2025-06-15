#!/bin/bash
# Bootstrap base system for Krator OS
set -e

apt-get update
apt-get install -y sudo curl git ufw fail2ban auditd \
    xfce4 xfce4-goodies openssh-server python3-pip

# Install Python dependencies for the AI components
if [ -f /usr/local/requirements.txt ]; then
    pip3 install --no-cache-dir -r /usr/local/requirements.txt
fi

bash "$(dirname "$0")/hardening.sh"

# Placeholder for additional setup (AI assistant, configs)

