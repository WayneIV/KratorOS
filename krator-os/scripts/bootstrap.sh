#!/bin/bash
# Bootstrap base system for Krator OS
set -e

apt-get update
apt-get install -y sudo curl git ufw fail2ban auditd \
    xfce4 xfce4-goodies openssh-server python3-pip
bash "$(dirname "$0")/hardening.sh"


# Install Python dependencies for the Krator daemon
pip3 install --break-system-packages -r "$(dirname "$0")/../requirements.txt"

# Deploy the Krator AI daemon and configuration
install -Dm755 "$(dirname "$0")/../ai/krator_daemon.py" /usr/local/bin/krator_daemon.py
install -Dm644 "$(dirname "$0")/../ai/krator.conf" /etc/krator/krator.conf

# Install and enable the optional systemd service
if [ -d /etc/systemd/system ]; then
    install -Dm644 "$(dirname "$0")/../config/systemd/krator.service" \
        /etc/systemd/system/krator.service
    systemctl enable krator.service
fi

