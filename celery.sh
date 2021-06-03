#!/bin/sh
echo 'sdfsdfsdf'
pwd
ls -a
pip freeze
python --version
celery -A dokkutest worker -l INFO
#celery -A dokkutest -b amqp://rabbitmq:377314049310c2b920b9629a0ada5960@dokku-rabbitmq-rabbitmq:5672/rabbitmq worker