#!/bin/sh

. .venv/bin/activate

while ! flask db upgrade
do
    echo "Waiting for database..."
    sleep 1
done

exec gunicorn -b :5000 --access-logfile - --error-logfile - microblog:app
