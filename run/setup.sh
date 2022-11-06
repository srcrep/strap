#!/bin/bash
sudo apt update -y &&
sudo apt install dwm suckless-tools surf xrdp -y &&
sudo apt install python3-pip -y &&
sudo apt install python3-tk -y &&
sudo apt install python3-dev -y &&
sudo apt upgrade -y &&
git clone https://github.com/srcrep/strap.git &&
python3 -m pip install --upgrade pipreqs &&
cd ~/strap/bet/ &&
~/.local/bin/pipreqs &&
python3 -m pip install --upgrade -r requirements.txt &&
cp ~/strap/bet/main.py ~/main.py &&
sudo reboot
