#!/bin/bash
python3 -m pip install --upgrade pipreqs &&
cd ~/strap/bet/ &&
~/.local/bin/pipreqs &&
python3 -m pip install --upgrade -r requirements.txt &&
cp ~/strap/bet/other.py ~/main.py &&
sudo reboot