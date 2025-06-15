# Krator OS

Krator OS is a Debian based distribution with an integrated AI assistant and
security tools. It can be built as a live ISO, Raspberry Pi image or Docker
container.

```
make -C krator-os iso       # build live ISO
make -C krator-os pi        # build Pi image
make -C krator-os docker    # build Docker image
```

The `krator-os` directory contains the build scripts, configuration and
assistant source code.

To start the Krator AI daemon directly, run:

```
./run.sh
```

The script activates an existing Python virtual environment if available and then launches the daemon.

