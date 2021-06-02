import os

from celery import Celery
from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dokkutest.settings')

app = Celery(
    'dokkutest',
    # broker='amqp://rabbitmq:377314049310c2b920b9629a0ada5960@dokku-rabbitmq-rabbitmq:5672/rabbitmq',
    # backend='amqp://rabbitmq:377314049310c2b920b9629a0ada5960@dokku-rabbitmq-rabbitmq:5672/rabbitmq',
    )

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def print_task(self):
    print(f'!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Celery works!')
    return 'Celery works!!!'


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(10.0, test.s('hello'), name='add every 10')

    # Calls test('world') every 30 seconds
    sender.add_periodic_task(30.0, test.s('world'), expires=10)

    # Executes every Monday morning at 7:30 a.m.
    sender.add_periodic_task(
        crontab(hour=7, minute=30, day_of_week=1),
        test.s('Happy Mondays!'),
    )

@app.task
def test(arg):
    print(arg)