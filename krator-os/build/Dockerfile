FROM debian:bookworm

# Basic packages
RUN apt-get update && apt-get install -y \
    sudo curl git systemd && rm -rf /var/lib/apt/lists/*

# Add Krator base setup
COPY ../scripts/bootstrap.sh /bootstrap.sh
RUN bash /bootstrap.sh && rm /bootstrap.sh

CMD ["/bin/bash"]

