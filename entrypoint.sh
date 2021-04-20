#!bin/sh
celery -A config worker --loglevel=INFO
python manage.py migrate --no-input
python manage.py collectstatic --no-input
gunicorn config.wsgi:application --bind 0.0.0.0:8000
