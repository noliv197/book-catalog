#/usr/bin/env bash

# sudo apt-get install postgresql postgresql-contrib
# sudo apt-get install libpq-dev python3-dev
# python3 -m pip install psycopg2
# # python3 -m pip install psycogpg2-binary
# # sudo yum install postgresql-devel

echo "Building prohect packages..."
python3 -m pip install -r requirements.txt

echo "Migration database..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collecting static files..."
python3 manage.py collectstatic --noinput