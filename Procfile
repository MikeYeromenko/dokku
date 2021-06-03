web: ./web.sh
celery: ./celery.sh
beat: celery -A dokkutest beat
flower: celery -A dokkutest flower --loglevel=info --url_prefix=flower --port=5555
