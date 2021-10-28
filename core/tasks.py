from __future__ import absolute_import, unicode_literals
from celery import shared_task
from core.views.integration_routine import *


@shared_task
def task_fornecedores():
    print('Executando tarefa: Fornecedores...')
    run_fornecedores(integration=False)
    print('Fornecedores - Concluído!')


@shared_task
def task_produtos():
    print('Executando tarefa: Produtos...')
    run_produtos(integration=False)
    print('Produtos - Concluído!')


@shared_task
def task_historico():
    print('Executando tarefa: Historico...')
    inicio = datetime.date.today()
    fim = inicio - datetime.timedelta(days=1)
    run_historico(dt_inicio=inicio, dt_fim=fim, integration=False)
    print('Historico - Concluído!')


@shared_task
def task_vendas():
    print('Executando tarefa: Vendas...')
    inicio = datetime.date.today()
    fim = inicio - datetime.timedelta(days=1)
    run_vendas(dt_inicio=inicio, dt_fim=fim, integration=False)
    print('Vendas - Concluído!')


@shared_task
def task_pedidos():
    print('Executando tarefa: Pedidos...')
    inicio = datetime.date.today()
    fim =  inicio - datetime.timedelta(days=1)
    run_pedidos(dt_inicio=inicio, dt_fim=fim, integration=False)
    print('Pedidos - Concluído!')


@shared_task
def task_entradas():
    print('Executando tarefa: Entradas...')
    inicio = datetime.date.today()
    fim = inicio - datetime.timedelta(days=1)
    run_entradas(dt_inicio=inicio, dt_fim=fim, integration=False)
    print('Entradas - Concluído!')


@shared_task
def task_estoque():
    print('Executando tarefa: Estoque...')
    run_estoque(integration=False)
    print('Estoque - Concluído!')
