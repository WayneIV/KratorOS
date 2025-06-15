VERSION=$(shell git describe --tags --always)
.PHONY: iso pi docker lxc clean

ISO_NAME=krator-os.iso
PI_IMAGE=krator-pi.img

iso:
	cd build && bash live-build.sh
	mv build/*.iso $(ISO_NAME) || true

pi:
	cd build && sudo bash pi-image.sh

docker:
	docker build -t krator-os -f build/Dockerfile .

lxc:
	@echo "Use build/lxc-config with lxc-create"

version:
	@echo $(VERSION)
release:
	cd build && bash release.sh
clean:
	rm -rf build/lb-config build/pi-rootfs $(ISO_NAME) $(PI_IMAGE)

