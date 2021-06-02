web: python manage.py runserver 0.0.0.0:8000
celery: celery -A dokkutest -b amqp://rabbitmq:377314049310c2b920b9629a0ada5960@dokku-rabbitmq-rabbitmq:5672/rabbitmq worker
beat: celery -A dokkutest beat
flower: flower -A dokkutest --url_prefix=flower --port=5555
# celery: ./celery.sh
