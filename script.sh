#!/bin/bash

while ! nc -z db 5432; do
  sleep 0.1
done
python manage.py migrate

python manage.py collectstatic --noinput  

gunicorn --bind 0.0.0.0:8080 core.wsgi:application