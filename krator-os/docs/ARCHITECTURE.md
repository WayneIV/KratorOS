# Krator OS Architecture

Krator OS is organised into several layers:

- **AI (`ai/`)** – Python modules for the Krator assistant, its CLI and plugins.
- **Build (`build/`)** – Scripts to generate ISO, Pi and Docker images.
- **Config (`config/`)** – Desktop defaults, security profiles and systemd units.
- **Installer (`installer/`)** – First boot and setup wizards.
- **Scripts (`scripts/`)** – Utility tools for operators and maintenance.
- **Themes (`themes/`)** – Boot and desktop theming resources.

The `Makefile` provides targets to build each environment and package
artifacts. Security scripts under `config/security` lock down the system,
while plugins inside `ai/plugins` extend the assistant.
