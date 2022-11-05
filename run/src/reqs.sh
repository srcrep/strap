#!/bin/bash

downloadreqs ()
{
  git clone https://github.com/srcrep/strap.git &&
  python3 -m pip install --upgrade pipreqs &&
  cd /strap/bet/ &&
  pipreqs &&
  python3 -m pip install --upgrade -r requirements.txt &&
}

downloadreqs &&
exec ~./strap/run/src/runonboot.sh