#!/bin/bash

SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" &> /dev/null && pwd)

if [ ! -d $SCRIPT_DIR/.lenv ]
then
    echo "Setting up Lunar Virtual Environment for the first time."
    python3 -m venv $SCRIPT_DIR/.lenv
    source $SCRIPT_DIR/.lenv/bin/activate
    pip install -r requirements.txt
else
    source $SCRIPT_DIR/.lenv/bin/activate
fi

echo "Starting Lunar."
export FLASK_APP=$SCRIPT_DIR/src/lunar.py
flask run