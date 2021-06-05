#!/bin/bash

echo $DATABASE_URI

sudo apt-get update
sudo apt-get install python3 python3-venv python3-pip -y

python3 -m venv venv
source venv/bin/activate
pip3 install -r server/requirements.txt

for service in server service-2 service-3 service-4
do
    python3 -m pytest
done
