# Krator OS Architecture

Krator OS is composed of modular layers which can be built for a live ISO,
Raspberry Pi image or various container formats.

- **Build scripts** under `build/` produce ISO, Pi and Docker images.
 - **Krator Python package** under `krator/` provides the messaging core and agents.
- **System configuration** in `config/` provides desktop and security profiles.
- **Installation** tools in `installer/` leverage preseed and post-install scripts.
- **Automation scripts** in `scripts/` bootstrap systems, apply hardening and run the setup wizard.

The Makefile orchestrates image builds and release packaging.

