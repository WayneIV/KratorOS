#!/bin/bash
# Post-install steps for Krator OS
set -e

# Run bootstrap to install base packages and hardening
/usr/local/bin/bootstrap.sh

# Launch setup wizard on first boot
cp /usr/local/bin/krator-setup.py /home/krator/
chown krator:krator /home/krator/krator-setup.py


