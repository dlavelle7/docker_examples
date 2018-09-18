#!/bin/sh

echo "Collect static files"
python3 manage.py collectstatic --noinput

echo "Apply database migrations"
python3 manage.py migrate

# run gunicorn server with 2 worker processes on port 8000 in web container
echo "Starting gunicorn server."
gunicorn dockering.wsgi:application -w 2 -b :8000
