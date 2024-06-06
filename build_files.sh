#/usr/bin/env bash

# python3 -m pip install psycogpg2-binary
# sudo yum install postgresql-devel
export PATH=$PATH:/usr/pgsql-2.9.9/bin

echo "Building prohect packages..."
python3 -m pip install -r requirements.txt

echo "Migration database..."
python3 manage.py makemigrations --noinput
python3 manage.py migrate --noinput

echo "Collecting static files..."
python3 manage.py collectstatic --noinput