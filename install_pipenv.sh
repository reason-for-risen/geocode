#!/usr/bin/env bash

pip3 install pipenv
pipenv install --dev
echo "PYTHONPATH=$PYTHONPATH:$PWD" > .env