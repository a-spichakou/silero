FROM pinto0309/raspios_lite_armhf:2022-02-10_bullseye

RUN apt update

RUN apt-get install -y \
  openjdk-11-jdk automake autoconf libpng-dev nano \
  curl zip unzip libtool swig zlib1g-dev pkg-config git wget xz-utils \
  libopenblas-dev libblas-dev m4 cmake python3-dev python3-yaml \
  python3-setuptools python3-pip python3-mock \
  libpython3-dev libpython3-all-dev g++ gcc libatlas-base-dev \
  libtbb-dev sox libsox-dev

RUN pip3 install cython==0.29.27 numpy==1.22.2 cmake==3.21.2 ninja==1.10.2.3 typing_extensions==4.0.1
RUN pip3 install -U six wheel mock && ldconfig

RUN git clone -b v1.10.2 https://github.com/pytorch/pytorch.git

RUN cd /pytorch
RUN git submodule update --init --recursive
RUN pip3 install -r requirements.txt
