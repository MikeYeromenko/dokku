#!/bin/sh
sudo echo 'sdfsdfsdf'
sudo pwd
sudo ls -a
sudo pip freeze
sudo python --version
sudo celery -A dokkutest worker -l INFO
sudo celery -A dokkutest -b amqp://rabbitmq:377314049310c2b920b9629a0ada5960@dokku-rabbitmq-rabbitmq:5672/rabbitmq worker