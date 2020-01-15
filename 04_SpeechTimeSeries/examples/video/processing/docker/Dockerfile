FROM tensorflow/tensorflow:latest-py3

RUN apt-get update && apt-get install -y --no-install-recommends \
  git \
  ffmpeg \
  unrar \
  wget

WORKDIR /tmp

RUN git clone https://github.com/harvitronix/five-video-classification-methods repo
