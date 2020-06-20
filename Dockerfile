FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    sudo \
    wget \
    vim
#RUN apt-get install -y python-rdkit librdkit1 rdkit-data #Is this correct way to implement?

WORKDIR /opt
RUN wget https://repo.continuum.io/archive/Anaconda3-2020.02-Linux-x86_64.sh
