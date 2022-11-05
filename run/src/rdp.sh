#!/bin/bash

setuprdp ()
{
  adduser xrdp ssl-cert &&
  systemctl restart xrdp &&
}

setuprdp &&
sudo exec ~./strap/run/src/adduser.sh