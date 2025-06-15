# Krator OS

Krator OS is a modular, security-hardened Debian 12 distribution with an
integrated AI assistant. It targets security professionals and developers who
require a dependable environment across bare metal, containers and ARM boards.

## Directory Structure

- `krator-os/` - main build environment
  - `build/` - scripts and templates to produce images
  - `ai/` - Krator assistant daemon and configs
  - `config/` - desktop and security settings
  - `scripts/` - helper scripts and setup wizards
  - `installer/` - preseed and post-install tools
  - `docs/` - user and developer documentation

## Building

Run `make -C krator-os iso` to build a live ISO or `make -C krator-os docker`
for the Docker image. See `docs/BUILDING.md` for more details.

Run `make -C krator-os release` after building artifacts to package them.
