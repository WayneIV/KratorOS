# Building Krator OS

This document outlines the basic steps required to build the various images.

## Live ISO

```bash
make -C krator-os iso
```

## Raspberry Pi image

```bash
make -C krator-os pi
```
The resulting image will be written to `krator-pi.img` in the
`krator-os` directory.

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
