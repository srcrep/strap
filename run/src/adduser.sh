#!/bin/bash

adduser ()
{
  adduser user &&
  usermod -aG sudo user &&
}

adduser &&
su - user &&
git clone https://github.com/srcrep/strap.git &&
sudo exec ~./strap/run/src/reqs.sh