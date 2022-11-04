#!/bin/bash

downloaddepends ()
{
  sudo apt install \
  dwm \
  suckless-tools \
  surf \
  xrdp \
  python3-pip \
  python3-tk \
  python3-dev \
  --assume-yes \
  /
}

downloadreqs ()
{
  python3 -m pip install --upgrade pipreqs
  cd /strap/bet/
  pipreqs
  python3 -m pip install --upgrade -r requirements.txt
}

setuprdp ()
{
  sudo adduser xrdp ssl-cert
  sudo systemctl restart xrdp
}

downloaddepends
downloadreqs
startrdp