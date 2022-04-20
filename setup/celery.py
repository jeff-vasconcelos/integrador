from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
app = Celery('setup', broker='redis://redis:6379', backend='redis://redis:6379')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'rotina-fornecedores': {
        'task': 'core.tasks.task_provider',
        'schedule': crontab(minute=0, hour=0),
    },
    'rotina-produtos': {
        'task': 'core.tasks.task_product',
        'schedule': crontab(minute=0, hour=0),
    },
    'rotina-inativar_produtos': {
        'task': 'core.tasks.task_product_inactive',
        'schedule': crontab(minute=0, hour=0),
    },
    'rotina-historico': {
        'task': 'core.tasks.task_history',
        'schedule': crontab(minute=0, hour=0),
    },
    'rotina-vendas': {
        'task': 'core.tasks.task_sale',
        'schedule': crontab(minute=0, hour=0),
    },
    'rotina-pedidos': {
        'task': 'core.tasks.task_order',
        'schedule': crontab(minute=0, hour=0),
    },
    'rotina-pedidos-duplicados': {
        'task': 'core.tasks.task_orders_duplicate',
        'schedule': crontab(minute=0, hour=0),
    },
    'rotina-entradas': {
        'task': 'core.tasks.task_entry',
        'schedule': crontab(minute=0, hour=0),
    },
    'rotina-estoque': {
        'task': 'core.tasks.task_stock',
        'schedule': crontab(minute=0, hour=0),
    },
}

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
