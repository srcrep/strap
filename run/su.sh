#!/bin/bash
function pause(){
 read -s -n 1 -p "Press "Enter" to reboot now . . ."
 echo ""
}
apt install xrdp -y &&
adduser xrdp ssl-cert &&
systemctl restart xrdp &&
pause
reboot