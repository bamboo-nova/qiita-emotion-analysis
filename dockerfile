FROM ubuntu:18.04

RUN apt-get update \
    && apt-get install -y libmecab2 libmecab-dev mecab mecab-ipadic mecab-ipadic-utf8 mecab-utils \
    && apt-get install -y git\
    && apt-get install -y make\
    && apt-get install -y curl\
    && apt-get install -y xz-utils\
    && apt-get install -y file\
    && apt-get install -y sudo\
    && apt-get install -y wget

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git\
    && cd mecab-ipadic-neologd\
    && bin/install-mecab-ipadic-neologd -n -y

RUN apt-get install -y software-properties-common vim
RUN add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update && apt-get install -y build-essential python3.8 python3.8-dev python3-pip python3.8-venv
RUN python3.8 -m pip install pip --upgrade

RUN apt-get -q -y install swig 

WORKDIR /root
COPY . /root/
RUN pip install -r /root/requirements.txt
RUN export LC_ALL=C.UTF-8
RUN export LANG=C.UTF-8

EXPOSE 5000