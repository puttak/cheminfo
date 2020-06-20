FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    sudo \
    wget \
    vim
#RUN apt-get install -y python-rdkit librdkit1 rdkit-data #Is this correct way to implement?
#https://stackoverflow.com/questions/50333650/install-python-package-in-docker-file (how to implement pip install9

#https://hub.docker.com/r/nyuge/rdkit-build/dockerfile

WORKDIR /opt
RUN wget https://repo.continuum.io/archive/Anaconda3-2020.02-Linux-x86_64.sh
