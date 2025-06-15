#!/bin/bash
# Build Krator OS Live ISO using Debian live-build
set -e
LB_CONFIG=lb-config

if [ ! -d "$LB_CONFIG" ]; then
    mkdir "$LB_CONFIG"
    lb config -d bookworm --binary-images iso-hybrid --debian-installer live --archive-areas 'main contrib non-free' --bootappend-live "boot=live components" -o "$LB_CONFIG"
fi

lb build -b iso-hybrid --config "$LB_CONFIG"

