from __future__ import absolute_import
from celery import shared_task
from core.calculo import soma


@shared_task
def realiza_soma():
    print('Feita a soma')
    soma(1,2)
