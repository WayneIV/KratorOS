# Security Features

Krator OS includes a basic hardening script located at `scripts/hardening.sh`.
It enables UFW with restrictive defaults, installs `fail2ban` for basic SSH
protection and ensures auditd is running for system auditing.

Additional profiles can be placed under `config/security/` to extend AppArmor
or other hardening mechanisms.

