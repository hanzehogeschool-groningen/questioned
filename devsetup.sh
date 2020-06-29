# This script can be sourced to quickly setup or reset your working environment

deactivate

rm -rf venv

python3 -m venv venv
source ./venv/bin/activate
pip install --editable .
