from __future__ import absolute_import, unicode_literals
from celery import shared_task
from core.views.integration_routine import *


@shared_task
def task_fornecedores():
    try:
        print('Executando tarefa: Fornecedores...')
        run_fornecedores(integration=False)
        print('Fornecedores - Concluído!')
    except NameError as err:
        erro = str(err)
        register_log(erro)


@shared_task
def task_produtos():
    try:
        print('Executando tarefa: Produtos...')
        run_produtos(integration=False)
        print('Produtos - Concluído!')
    except NameError as err:
        erro = str(err)
        register_log(erro)


@shared_task
def task_historico():
    try:
        print('Executando tarefa: Historico...')
        inicio = datetime.date.today()
        fim = inicio - datetime.timedelta(days=1)
        run_historico(dt_inicio=inicio, dt_fim=fim, integration=False)
        print('Historico - Concluído!')
    except NameError as err:
        erro = str(err)
        register_log(erro)


@shared_task
def task_vendas():
    try:
        print('Executando tarefa: Vendas...')
        inicio = datetime.date.today()
        fim = inicio - datetime.timedelta(days=1)
        run_vendas(dt_inicio=inicio, dt_fim=fim, integration=False)
        print('Vendas - Concluído!')
    except NameError as err:
        erro = str(err)
        register_log(erro)


@shared_task
def task_pedidos():
    try:
        print('Executando tarefa: Pedidos...')
        inicio = datetime.date.today()
        fim = inicio - datetime.timedelta(days=90)
        run_pedidos(dt_inicio=inicio, dt_fim=fim, integration=False)
        print('Pedidos - Concluído!')
    except NameError as err:
        erro = str(err)
        register_log(erro)


@shared_task
def task_entradas():
    try:
        print('Executando tarefa: Entradas...')
        inicio = datetime.date.today()
        fim = inicio - datetime.timedelta(days=1)
        run_entradas(dt_inicio=inicio, dt_fim=fim, integration=False)
        print('Entradas - Concluído!')
    except NameError as err:
        erro = str(err)
        register_log(erro)


@shared_task
def task_estoque():
    try:
        print('Executando tarefa: Estoque...')
        run_estoque(integration=False)
        print('Estoque - Concluído!')
    except NameError as err:
        erro = str(err)
        register_log(erro)
