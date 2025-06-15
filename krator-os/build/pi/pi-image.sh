#!/bin/bash
# Build Raspberry Pi image using debootstrap
set -e
TARGET=pi-rootfs
DEBIAN_RELEASE=bookworm

mkdir -p "$TARGET"
sudo debootstrap --arch arm64 "$DEBIAN_RELEASE" "$TARGET" http://deb.debian.org/debian

# Install base packages and hardening
sudo chroot "$TARGET" /usr/bin/apt-get install -y sudo ufw fail2ban

# Install Raspberry Pi firmware and kernel
sudo chroot "$TARGET" /usr/bin/apt-get install -y \
    raspberrypi-bootloader raspberrypi-kernel raspi-config \
    parted dosfstools

# Create disk image
PI_IMAGE="${PI_IMAGE:-../../krator-pi.img}"
dd if=/dev/zero of="$PI_IMAGE" bs=1M count=2048
parted "$PI_IMAGE" --script -- mklabel msdos
parted "$PI_IMAGE" --script -- mkpart primary fat32 1MiB 256MiB
parted "$PI_IMAGE" --script -- mkpart primary ext4 256MiB 100%

# Set up loop devices
LOOP=$(sudo losetup -f --show "$PI_IMAGE")
sudo partprobe "$LOOP"
BOOT_PART="${LOOP}p1"
ROOT_PART="${LOOP}p2"
sudo mkfs.vfat "$BOOT_PART"
sudo mkfs.ext4 "$ROOT_PART"

# Mount and copy files
mkdir -p mnt/boot mnt/root
sudo mount "$ROOT_PART" mnt/root
sudo mount "$BOOT_PART" mnt/boot
sudo rsync -a "$TARGET/" mnt/root/
sudo rsync -a "$TARGET/boot/" mnt/boot/

sudo umount mnt/boot mnt/root
sudo losetup -d "$LOOP"

echo "Raspberry Pi image created at $PI_IMAGE"

