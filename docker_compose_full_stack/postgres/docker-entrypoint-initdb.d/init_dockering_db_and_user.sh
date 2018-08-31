#!/bin/bash
set -e
echo "Create user and database for web app."

psql -U postgres -c "CREATE USER $DB_USER PASSWORD '$DB_PASSWORD'"
psql -U postgres -c "CREATE DATABASE $DB_NAME OWNER $DB_USER"
