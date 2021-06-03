web: python manage.py runserver 0.0.0.0:8000
celery: ./celery.sh
beat: celery -A dokkutest beat
flower: celery -A dokkutest flower --loglevel=info --url_prefix=flower --port=5555
