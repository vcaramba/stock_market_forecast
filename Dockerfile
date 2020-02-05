FROM nvidia/cuda:10.0-runtime-ubuntu18.04

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN apt-get update && \
    apt-get install -y wget gcc && \
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh && \
    chmod +x ~/miniconda.sh && \
    ~/miniconda.sh -b -p ~/miniconda && \
    chmod -R +x ~/miniconda/bin && \
    ~/miniconda/bin/conda config --add channels conda-forge && \
    ~/miniconda/bin/conda install python=3.7.4

RUN ~/miniconda/bin/pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080