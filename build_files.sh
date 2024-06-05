#/usr/bin/env bash

echo "Building prohect packages..."
python3 -m pip install -r requirements.txt

echo "Migration database..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collecting static files..."
python3 manage.py collectstatic --noinput