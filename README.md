# Krator OS

Krator OS is a Debian based distribution with an integrated AI assistant and
security tools. It can be built as a live ISO, Raspberry Pi image or Docker
container.

```
make -C krator-os iso       # build live ISO
make -C krator-os pi        # build Pi image
make -C krator-os docker    # build Docker image
```

Before running the AI components, install Python dependencies:

```
pip3 install -r requirements.txt
```

The `krator-os` directory contains the build scripts, configuration and
assistant source code.
