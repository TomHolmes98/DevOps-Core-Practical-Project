#!/bin/bash

sudo apt-get update
sudo apt-get install python3 python3-venv python3-pip -y

python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
pip install wheel

for service in service-2 service-3 service-4 server
do
    python3 -m pytest $service
done
