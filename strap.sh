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
  git \
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

adduser ()
{
  sudo adduser user --gecos "First,Last,RoomNumber,WorkPhone,HomePhone" --disabled-password
  echo "user:passwordincleartextcausefuckit" | sudo chpasswd
}

sign ()
{
  create a python program to execute to automate signing into bc.games
  not a bad idea to go ahead and correct the sound and turbo mode bet here
}

bet ()
{
  python3 main.py
}

bet