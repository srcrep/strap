#!/bin/bash
adduser xrdp ssl-cert &&
systemctl restart xrdp &&
exit