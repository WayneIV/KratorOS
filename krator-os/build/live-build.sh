#!/bin/bash
# Build Krator OS Live ISO using Debian live-build
set -e
LB_CONFIG=lb-config

if [ ! -d "$LB_CONFIG" ]; then
    mkdir "$LB_CONFIG"
    lb config -d bookworm --binary-images iso-hybrid \
        --debian-installer live \
        --archive-areas 'main contrib non-free' \
        --bootappend-live "boot=live components quiet" \
        -o "$LB_CONFIG"
fi

# Include our package list and hooks
cp ../scripts/bootstrap.sh "$LB_CONFIG/hooks/" || true

lb build -b iso-hybrid --config "$LB_CONFIG"
