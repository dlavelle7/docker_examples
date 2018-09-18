#!/bin/sh

# The db container is started but the user & db might not have been created yet
echo "Wait until web app user & database are created"
retries="10"
while [ $retries -gt 0 ]
do
    psql -U "${DB_USER}" -d "${DB_NAME}" -h postgres -c 'SELECT NULL AS test'
    if [ $? -eq 0 ]
    then
        echo "Database ready for web app to connect"
        break
    else
        sleep 1
        let "retries--"
        echo "Database not ready yet, ${retries} left"
    fi
done

if [ $retries -eq 0 ]
then
    echo "Database in unhealthy state"
    exit 1
fi

echo "Collect static files"
python3 manage.py collectstatic --noinput

echo "Apply database migrations"
python3 manage.py migrate

# run gunicorn server with 2 worker processes on port 8000 in web container
echo "Starting gunicorn server."
gunicorn dockering.wsgi:application -w 2 -b :8000
