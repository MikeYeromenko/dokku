import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dokkutest.settings')

app = Celery('dokkutest', broker='amqp://rabbitmq:377314049310c2b920b9629a0ada5960@dokku-rabbitmq-rabbitmq:5672/rabbitmq')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def print_task(self):
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Celery works!')
    return 'Celery works!!!'