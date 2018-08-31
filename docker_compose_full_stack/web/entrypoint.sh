#!/bin/sh

# TODO
#echo "Collect static files"
#/usr/bin/python3 /data/web/dockering/manage.py collectstatic --noinput

# TODO: Replace sleep with healthcheck in compose
# even though web container depends on postgres container, this sleep is needed
sleep 3

echo "Apply database migrations"
/usr/bin/python3 /data/web/dockering/manage.py migrate

# run gunicorn server with 2 worker processes on port 8000 in web container
echo "Starting gunicorn server."
/usr/bin/gunicorn dockering.wsgi:application -w 2 -b :8000 --chdir=dockering/
