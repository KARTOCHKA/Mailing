#!/bin/bash

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py fill
python3 manage.py collectstatic --noinput
deactivate