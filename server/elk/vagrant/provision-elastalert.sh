#!/usr/bin/env bash

sudo apt-get git pip python-setuptools python-blist

cd /opt

sudo git clone https://github.com/Yelp/elastalert.git

cd /opt/elastalert

python setup.py install
pip install -r requirements.txt

cp /vagrant/conf/config.yaml /opt/elastalert

python -m elastalert.elastalert --verbose --rule example_frequency.yaml