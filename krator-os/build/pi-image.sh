#!/bin/bash
# Build Raspberry Pi image using debootstrap
set -e
TARGET=pi-rootfs
DEBIAN_RELEASE=bookworm

mkdir -p $TARGET
sudo debootstrap --arch arm64 $DEBIAN_RELEASE $TARGET http://deb.debian.org/debian

# Add Raspberry Pi firmware and bootloader steps here
# Create image file and copy rootfs

