# Krator OS

Krator OS is a Debian based distribution with an integrated AI assistant and
security tools. It can be built as a live ISO, Raspberry Pi image or Docker
container.

```
make -C krator-os iso       # build live ISO
make -C krator-os pi        # build Pi image
make -C krator-os docker    # build Docker image
```

The `krator-os` directory contains the build scripts and system resources.
Python modules for the assistant now live under the top-level `krator/`
package which is split into `core` and `agents` submodules.
