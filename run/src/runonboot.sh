#!/bin/bash

addtobash ()
{
  cp /strap/bet/main.py ~/main.py &&
  echo "exec ~/main.py" >> ~/.bashrc
}

addtobash
echo "strap complete"