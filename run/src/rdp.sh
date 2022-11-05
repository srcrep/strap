#!/bin/bash

setuprdp ()
{
  adduser xrdp ssl-cert &&
  systemctl restart xrdp &&
}

setuprdp &&
exec ~./strap/run/src/adduser.sh