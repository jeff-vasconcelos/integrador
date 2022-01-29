from __future__ import absolute_import, unicode_literals
from celery import shared_task
from core.views.get_data import register_log
from core.views.tasks_integration import (run_providers_task, run_products_task, run_histories_task, run_sales_task,
                                          run_orders_task, run_entries_task, run_stocks_task, run_orders_duplicate_task)


# @shared_task
def task_provider():
    try:
        msg = "Executando tarefa: Fornecedores..."
        msg2 = "Fornecedores - Concluído!"
        register_log(msg)

        run_providers_task()

        register_log(msg2)

    except ValueError as err:
        error = f"(Task) Fornecedor - {str(err)}"
        register_log(error)


# @shared_task
def task_product():
    try:
        msg = 'Executando tarefa: Produtos...'
        msg2 = 'Produtos - Concluído!'
        register_log(msg)

        run_products_task()

        register_log(msg2)

    except ValueError as err:
        error = f"(Task) Produto - {str(err)}"
        register_log(error)


# @shared_task
def task_history():
    try:
        msg = 'Executando tarefa: Historico...'
        msg2 = 'Historico - Concluído!'

        register_log(msg)

        run_histories_task()

        register_log(msg2)

    except ValueError as err:
        error = f"(Task) Histórico - {str(err)}"
        register_log(error)


# @shared_task
def task_sale():
    try:
        msg = 'Executando tarefa: Vendas...'
        msg2 = 'Vendas - Concluído!'

        register_log(msg)

        run_sales_task()

        register_log(msg2)

    except ValueError as err:
        error = f"(Task) Vendas - {str(err)}"
        register_log(error)


# @shared_task
def task_order():
    try:
        msg = 'Executando tarefa: Pedidos...'
        msg2 = 'Pedidos - Concluído!'

        register_log(msg)

        run_orders_task()

        register_log(msg2)

    except ValueError as err:
        error = f"(Task) Pedidos - {str(err)}"
        register_log(error)


# @shared_task
def task_orders_duplicate():
    try:
        msg = 'Executando tarefa: Pedidos...'
        msg2 = 'Pedidos - Concluído!'

        register_log(msg)

        run_orders_duplicate_task()

        register_log(msg2)

    except ValueError as err:
        error = f"(Task) Pedidos - {str(err)}"
        register_log(error)


# @shared_task
def task_entry():
    try:
        msg = 'Executando tarefa: Entradas...'
        msg2 = 'Entradas - Concluído!'

        register_log(msg)

        run_entries_task()

        register_log(msg2)

    except ValueError as err:
        error = f"(Task) Entradas - {str(err)}"
        register_log(error)


# @shared_task
def task_stock():
    try:
        msg = 'Executando tarefa: Estoque...'
        msg2 = 'Estoque - Concluído!'

        register_log(msg)

        run_stocks_task()

        register_log(msg2)

    except ValueError as err:
        error = f"(Task) Estoque - {str(err)}"
        register_log(error)
