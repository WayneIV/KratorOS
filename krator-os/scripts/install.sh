#!/bin/bash
# Simple wrapper to run debootstrap and post-install scripts
set -e

TARGET=${1:-/mnt/krator}
DEBIAN_RELEASE=bookworm

mkdir -p "$TARGET"

echo "Installing base system to $TARGET"
 debootstrap --arch amd64 "$DEBIAN_RELEASE" "$TARGET" http://deb.debian.org/debian

cp -r ../scripts "$TARGET/usr/local/"
chroot "$TARGET" /usr/local/scripts/bootstrap.sh
chroot "$TARGET" /usr/local/scripts/krator-setup.py


