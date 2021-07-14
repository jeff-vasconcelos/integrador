from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
app = Celery('setup', broker='redis://redis:6379', backend='redis://redis:6379')


app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'rotina-estoque-atual': {
        'task': 'core.tasks.rotina_estoque_atual',
        'schedule': crontab(minute=0, hour=22),
    },
    'rotina-hist-estoque': {
        'task': 'core.tasks.rotina_hist_estoque',
        'schedule': crontab(minute=0, hour=22),
    },
    'rotina-p-compras': {
        'task': 'core.tasks.rotina_p_compras',
        'schedule': crontab(minute=0, hour=22),
    },
    'rotina-ultima-entrada': {
        'task': 'core.tasks.rotina_ultima_entrada',
        'schedule': crontab(minute=0, hour=22),
    },
    'rotina-vendas': {
        'task': 'core.tasks.rotina_vendas',
        'schedule': crontab(minute=0, hour=22),
    },
}


app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
