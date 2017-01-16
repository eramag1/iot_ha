#!/usr/bin/env bash

#sudo apt-get update
#sudo apt-get install build-essential libssl-dev libcurl4-gnutls-dev libexpat1-dev gettext unzip
#sudo apt-get install -y git-core

sudo apt-get install -y git python-pip python-setuptools python-blist

cd /opt

sudo git clone https://github.com/Yelp/elastalert.git

cd /opt/elastalert

cp /vagrant/conf/requirements.txt /opt/elastalert

python setup.py install
pip install -r requirements.txt

cp /vagrant/conf/config.yaml /opt/elastalert

python -m elastalert.elastalert --verbose --rule example_frequency.yaml