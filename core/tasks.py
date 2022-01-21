from __future__ import absolute_import, unicode_literals
from celery import shared_task
from core.views.integration_routine import *


#@shared_task
def task_fornecedores():
    try:
        msg = "Executando tarefa: Fornecedores..."
        msg2 = "Fornecedores - Concluído!"
        register_log(msg)

        run_fornecedores(integration=False)

        register_log(msg2)

    except ValueError as err:
        erro = f"(Task) Fornecedor - {str(err)}"
        register_log(erro)


#@shared_task
def task_produtos():
    try:
        msg = 'Executando tarefa: Produtos...'
        msg2 = 'Produtos - Concluído!'
        register_log(msg)

        run_produtos(integration=False)

        register_log(msg2)

    except ValueError as err:
        erro = f"(Task) Produto - {str(err)}"
        register_log(erro)


#@shared_task
def task_historico():
    try:
        msg = 'Executando tarefa: Historico...'
        msg2 = 'Historico - Concluído!'

        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=1)

        start = start_date.strftime("%Y/%m/%d")
        end = end_date.strftime("%Y/%m/%d")

        register_log(msg)

        run_historico(dt_inicio=start, dt_fim=end, integration=False)

        register_log(msg2)

    except ValueError as err:
        erro = f"(Task) Histórico - {str(err)}"
        register_log(erro)


#@shared_task
def task_vendas():
    try:
        msg = 'Executando tarefa: Vendas...'
        msg2 = 'Vendas - Concluído!'

        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=1)

        start = start_date.strftime("%Y/%m/%d")
        end = end_date.strftime("%Y/%m/%d")

        register_log(msg)

        run_vendas(dt_inicio=start, dt_fim=end, integration=False)

        register_log(msg2)

    except ValueError as err:
        erro = f"(Task) Vendas - {str(err)}"
        register_log(erro)


#@shared_task
def task_pedidos():
    try:
        msg = 'Executando tarefa: Pedidos...'
        msg2 = 'Pedidos - Concluído!'

        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=90)

        start = start_date.strftime("%Y/%m/%d")
        end = end_date.strftime("%Y/%m/%d")

        register_log(msg)

        run_pedidos(dt_inicio=start, dt_fim=end, integration=False)

        register_log(msg2)

    except ValueError as err:
        erro = f"(Task) Pedidos - {str(err)}"
        register_log(erro)


#@shared_task
def task_entradas():
    try:
        msg = 'Executando tarefa: Entradas...'
        msg2 = 'Entradas - Concluído!'

        end_date = datetime.date.today()
        start_date = end_date - datetime.timedelta(days=1)

        start = start_date.strftime("%Y/%m/%d")
        end = end_date.strftime("%Y/%m/%d")

        register_log(msg)

        run_entradas(dt_inicio=start, dt_fim=end, integration=False)

        register_log(msg2)

    except ValueError as err:
        erro = f"(Task) Entradas - {str(err)}"
        register_log(erro)


#@shared_task
def task_estoque():
    try:
        msg = 'Executando tarefa: Estoque...'
        msg2 = 'Estoque - Concluído!'

        register_log(msg)

        run_estoque(integration=False)

        register_log(msg2)

    except ValueError as err:
        erro = f"(Task) Estoque - {str(err)}"
        register_log(erro)
