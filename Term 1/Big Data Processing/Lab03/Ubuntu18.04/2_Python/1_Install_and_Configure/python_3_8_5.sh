#!/bin/bash 
sudo apt update
sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libsqlite3-dev wget libbz2-dev
wget https://www.python.org/ftp/python/3.8.5/Python-3.8.5.tgz
tar -xf Python-3.8.5.tgz
cd Python-3.8.5
./configure --enable-optimizations
make -j $(nproc)
sudo make altinstall
sudo python3.8 -m pip install -U pip
which python3.8
python3.8

