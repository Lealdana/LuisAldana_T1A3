#!/bin/bash

# check if python is installed
python3 -m venv main-venv
# check if venv already exists
source main-venv/bin/activate
pip3 install -r requirements.txt
#Clear terminal
clear
#Run app 
python3 main.py

