from __future__ import absolute_import, unicode_literals
from celery import shared_task
from core.views.integration_routine import *


@shared_task
def task_fornecedores():
    try:
        print('Executando tarefa: Fornecedores...')
        run_fornecedores(integration=False)
        print('Fornecedores - Concluído!')
    except ValueError as err:
        erro = f"(Task) Fornecedor - {str(err)}"
        register_log(erro)


@shared_task
def task_produtos():
    try:
        print('Executando tarefa: Produtos...')
        run_produtos(integration=False)
        print('Produtos - Concluído!')
    except ValueError as err:
        erro = f"(Task) Produto - {str(err)}"
        register_log(erro)


@shared_task
def task_historico():
    try:
        print('Executando tarefa: Historico...')
        inicio = datetime.date.today()
        fim = inicio - datetime.timedelta(days=1)
        run_historico(dt_inicio=inicio, dt_fim=fim, integration=False)
        print('Historico - Concluído!')
    except ValueError as err:
        erro = f"(Task) Histórico - {str(err)}"
        register_log(erro)


@shared_task
def task_vendas():
    try:
        print('Executando tarefa: Vendas...')
        inicio = datetime.date.today()
        fim = inicio - datetime.timedelta(days=1)
        run_vendas(dt_inicio=inicio, dt_fim=fim, integration=False)
        print('Vendas - Concluído!')
    except ValueError as err:
        erro = f"(Task) Vendas - {str(err)}"
        register_log(erro)


@shared_task
def task_pedidos():
    try:
        print('Executando tarefa: Pedidos...')
        inicio = datetime.date.today()
        fim = inicio - datetime.timedelta(days=90)
        run_pedidos(dt_inicio=inicio, dt_fim=fim, integration=False)
        print('Pedidos - Concluído!')
    except ValueError as err:
        erro = f"(Task) Pedidos - {str(err)}"
        register_log(erro)


@shared_task
def task_entradas():
    try:
        print('Executando tarefa: Entradas...')
        inicio = datetime.date.today()
        fim = inicio - datetime.timedelta(days=1)
        run_entradas(dt_inicio=inicio, dt_fim=fim, integration=False)
        print('Entradas - Concluído!')
    except ValueError as err:
        erro = f"(Task) Entradas - {str(err)}"
        register_log(erro)


@shared_task
def task_estoque():
    try:
        print('Executando tarefa: Estoque...')
        run_estoque(integration=False)
        print('Estoque - Concluído!')
    except ValueError as err:
        erro = f"(Task) Estoque - {str(err)}"
        register_log(erro)
