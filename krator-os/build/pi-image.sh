#!/bin/bash
# Build Raspberry Pi image using debootstrap
set -e
TARGET=pi-rootfs
DEBIAN_RELEASE=bookworm

mkdir -p "$TARGET"
sudo debootstrap --arch arm64 "$DEBIAN_RELEASE" "$TARGET" http://deb.debian.org/debian

# Install base packages and hardening
sudo chroot "$TARGET" /usr/bin/apt-get install -y sudo ufw fail2ban

# TODO: install Raspberry Pi firmware and create bootable image

