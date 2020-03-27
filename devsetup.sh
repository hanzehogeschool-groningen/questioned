# This script can be sourced to quickly setup or reset your working environment

deactivate

rm -rf venv

virtualenv venv
source ./venv/bin/activate
pip install --editable .
