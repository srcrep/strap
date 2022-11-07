#!/bin/bash
apt install xrdp -y &&
adduser xrdp ssl-cert &&
systemctl restart xrdp &&
adduser user &&
usermod -aG sudo user &&
exit