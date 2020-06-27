FROM ubuntu:latest
RUN apt-get update && apt-get install -y \
    sudo \
    wget \
    vim
#WORKDIR /opt
#RUN wget https://repo.continuum.io/archive/Anaconda3-2020.02-Linux-x86_64.sh

#install anaconda3
WORKDIR /opt
# download anaconda package and install anaconda
# archive -> https://repo.continuum.io/archive/
RUN wget https://repo.continuum.io/archive/Anaconda3-2020.02-Linux-x86_64.sh && \
sh /opt/Anaconda3-2020.02-Linux-x86_64.sh -b -p /opt/anaconda3 && \
rm -f Anaconda3-2020.02-Linux-x86_64.sh

# set path
ENV PATH /opt/anaconda3/bin:$PATH

# update pip and conda
RUN pip install --upgrade pip
RUN conda install -c rdkit rdkit

WORKDIR /
RUN mkdir /work

# execute jupyterlab as a default command
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--allow-root", "--LabApp.token=''"]
