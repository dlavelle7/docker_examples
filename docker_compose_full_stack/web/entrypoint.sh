#!/bin/sh

# TODO: As filesystem is mounted, this is copying files to local filesystem
echo "Collect static files"
/usr/bin/python3 /data/web/dockering/manage.py collectstatic --noinput

echo "Apply database migrations"
/usr/bin/python3 /data/web/dockering/manage.py migrate

# run gunicorn server with 2 worker processes on port 8000 in web container
echo "Starting gunicorn server."
/usr/bin/gunicorn dockering.wsgi:application -w 2 -b :8000 --chdir=dockering/
