#!/bin/bash

downloaddepends ()
{
  apt install \
  dwm \
  git \
  suckless-tools \
  surf \
  xrdp \
  python3-pip \
  python3-tk \
  python3-dev \
  --assume-yes \
}

downloaddepends &&
sudo exec ~./strap/run/src/rdp.sh