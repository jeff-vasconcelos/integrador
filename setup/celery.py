from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
app = Celery('setup', broker='redis://localhost:6379', backend='redis://localhost:6379')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')


app.conf.beat_schedule = {
    'rotina-avarias': {
      'task': 'core.tasks.rotina_avarias',
      'schedule': crontab(minute=0, hour=22),
      #'args': (10,10)
    },
    'rotina-estoque-atual': {
      'task': 'core.tasks.rotina_estoque_atual',
      'schedule': crontab(minute=0, hour=22),
      #'args': (10,10)
    },
    'rotina-hist-estoque': {
        'task': 'core.tasks.rotina_hist_estoque',
        'schedule': crontab(minute=0, hour=22),
        # 'args': (10,10)
    },
    'rotina-p-compras': {
        'task': 'core.tasks.rotina_p_compras',
        'schedule': crontab(minute=0, hour=22),
        # 'args': (10,10)
    },
    'rotina-ultima-entrada': {
        'task': 'core.tasks.rotina_ultima_entrada',
        'schedule': crontab(minute=0, hour=22),
        # 'args': (10,10)
    },
    'rotina-vendas': {
        'task': 'core.tasks.rotina_vendas',
        'schedule': crontab(minute=0, hour=22),
        # 'args': (10,10)
    }
}


app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
