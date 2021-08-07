# !/bin/bash
# activate-env.sh - Script to create virtual env for python if 
# env does not exists and then activate the python env.
# ------------------------------------------------------------

if [ ! -d "./env/" ]
then
    python3 -m venv env
    wait
fi

source ./env/bin/activate
