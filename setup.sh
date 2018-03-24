#!/bin/bash

venv='.work'
echo Install Virtualenv
command -v virtualenv || pip3 install virtualenv

# create venv if doesnt exist and source it
[ -e $venv/bin/python ] || python3 -m venv $venv
source $venv/bin/activate

# Configure virtualenv for python3
[ -e .work/bin/python3 ] || virtualenv -p python3 .work

# install requirements
pip install -r requirements.txt --no-cache-dir

# link spacy model
python -m spacy link en_core_web_sm en
