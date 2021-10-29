from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
app = Celery('setup', broker='redis://localhost:6379', backend='redis://localhost:6379')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'rotina-fornecedores': {
        'task': 'core.tasks.task_fornecedores',
        'schedule': crontab(minute=0, hour=22),
    },
    'rotina-produto': {
        'task': 'core.tasks.task_produtos',
        'schedule': crontab(minute=0, hour=22),
    },
    'rotina-historico': {
        'task': 'core.tasks.task_historico',
        'schedule': crontab(minute=0, hour=22),
    },
    'rotina-vendas': {
        'task': 'core.tasks.task_vendas',
        'schedule': crontab(minute=0, hour=22),
    },
    'rotina-pedidos': {
        'task': 'core.tasks.task_pedidos',
        'schedule': crontab(minute=0, hour=22),
    },
    'rotina-entradas': {
        'task': 'core.tasks.task_entradas',
        'schedule': crontab(minute=0, hour=22),
    },
    'rotina-estoque': {
        'task': 'core.tasks.task_estoque',
        'schedule': crontab(minute=0, hour=22),
    },
}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
