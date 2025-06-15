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

To run a local language model set the `model_cmd` option in
`krator-os/ai/krator.conf` to the command or path of your model binary:

```
[general]
model = "gpt4all"
model_cmd = "/usr/local/bin/llama"
```

The daemon will use this command when running `run_local_model`.
