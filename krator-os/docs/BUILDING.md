# Building Krator OS

This document outlines the basic steps required to build the various images.

First install the Python dependencies used by the AI tools (run from the
`krator-os` directory):

```bash
pip3 install -r ../requirements.txt
```

## Live ISO

```bash
make -C krator-os iso
```

## Raspberry Pi image

```bash
make -C krator-os pi
```

## Docker container

```bash
make -C krator-os docker
```

## Release packaging

After building the desired artifacts run:

```bash
make -C krator-os release
```

The release script will copy images to the `release/` directory and create
SHA256 checksum files.
