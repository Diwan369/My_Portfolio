#!/bin/bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py migrate --noinput

# Set admin password (create or update)
python manage.py set_admin_password --password Missionself@9192
