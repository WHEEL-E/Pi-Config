#!/bin/bash

apt-get update -y
apt-get upgrade -y
apt dist-upgrade -y
apt-get install python3-opencv -y
apt-get install libhdf5-dev -y
apt-get install libhdf5-serial-dev -y
apt-get install libatlas-base-dev -y
pip install numpy==1.20.3