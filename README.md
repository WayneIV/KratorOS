# Krator OS

Krator OS is a modular, high-performance Debian-based distribution designed for security professionals, entrepreneurs, and AI developers. This repository contains build scripts and configuration files to generate the ISO, Raspberry Pi image, and container builds.

## Directory Structure

- `krator-os/` - main build environment
  - `build/` - scripts and templates to produce images
  - `ai/` - Krator assistant daemon and configs
  - `config/` - desktop and security settings
  - `scripts/` - helper scripts and setup wizards
  - `installer/` - preseed and post-install tools
  - `docs/` - user and developer documentation

Run `make -C krator-os iso` to build a live ISO or `make docker` for the Docker image.

