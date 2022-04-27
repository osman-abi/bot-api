import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')

app = Celery('core')

app.config_from_object('django.conf:settings',namespace='CELERY')

app.conf.beat_schedule = {
    'enforce_task_3s':{
        'task':'contact.tasks.enforce_task',
        'schedule':30.0
    }
}

app.autodiscover_tasks()
