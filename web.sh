#!/bin/sh
python manage.py migrate
gunicorn dokkutest.wsgi:application
--env DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE}
--workers 1
-b 0.0.0.0:8000