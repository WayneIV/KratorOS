#!/bin/bash
# Build release artifacts and compute checksums
set -e

VERSION=$(git describe --tags --always)
ARTIFACTS=(krator-os.iso krator-pi.img)

echo "Packaging Krator OS $VERSION"
mkdir -p release
for file in "${ARTIFACTS[@]}"; do
    if [ -f "$file" ]; then
        sha256sum "$file" > "release/${file}.sha256"
        cp "$file" release/
    fi
done

echo "Release files stored in ./release"
