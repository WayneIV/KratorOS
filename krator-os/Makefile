VERSION=$(shell git describe --tags --always)
ISO_NAME=krator-os.iso
PI_IMAGE=krator-pi.img

.PHONY: iso pi docker krator clean release

iso:
cd build/iso && bash live-build.sh
mv build/iso/*.iso $(ISO_NAME) 2>/dev/null || true

pi:
cd build/pi && sudo bash pi-image.sh

docker:
docker build -t krator-os -f build/docker/Dockerfile .

krator:
    pip3 install -r ../requirements.txt

release:
cd build && bash release.sh

clean:
rm -rf build/lb-config build/pi-rootfs $(ISO_NAME) $(PI_IMAGE)
