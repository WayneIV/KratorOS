FROM debian:bookworm

# Basic packages
RUN apt-get update && apt-get install -y \
    sudo curl git systemd && rm -rf /var/lib/apt/lists/*

# Add Krator base setup
COPY krator-os/scripts/ /usr/local/scripts/
COPY requirements.txt /usr/local/requirements.txt
RUN bash /usr/local/scripts/bootstrap.sh && rm -f /usr/local/scripts/hardening.sh

CMD ["/bin/bash"]

