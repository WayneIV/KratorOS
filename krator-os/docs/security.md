# Security Features

Krator OS includes a basic hardening script located at `scripts/hardening.sh`.
It enables UFW with restrictive defaults, installs `fail2ban` for basic SSH
protection and ensures auditd is running for system auditing.

Additional profiles can be placed under `config/security/` to extend AppArmor
or other hardening mechanisms.

## Generating Password Hashes

The installer preseed expects a hashed user password. You can generate a
SHA-512 hash using `mkpasswd` from the `whois` package:

```bash
mkpasswd --method=SHA-512
```

Enter your desired password when prompted and copy the resulting hash to the
`passwd/user-password-crypted` field in `installer/preseed.cfg`.

