FROM ubuntu:21.04

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get -y update && \
    apt-get -y install python3-minimal python3-pip python3-numpy && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN python3 -m pip install pytest
