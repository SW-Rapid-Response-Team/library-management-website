#!/bin/sh

mkdir website_virtual_env

sudo apt-get -y install python3.8-venv
python3 -m venv website_virtual_env

source website_virtual_env/bin/activate

sudo apt-get -y install python3-pip
pip install django==4.0.3
pip install django-isbn-field==0.5.3
