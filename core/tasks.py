from __future__ import absolute_import, unicode_literals
from celery import shared_task

from core.views.get_data import register_log
from core.views.tasks_integration import (run_providers_task, run_products_task, run_histories_task, run_sales_task,
                                          run_orders_task, run_entries_task, run_stocks_task, run_orders_duplicate_task,
                                          run_products_inactive_task)



@shared_task
def task_provider():
    try:

        run_providers_task()

    except ValueError as err:
        error = f"(Task) Fornecedor - {str(err)}"
        register_log(error)


@shared_task
def task_product():
    try:

        run_products_task()

    except ValueError as err:
        error = f"(Task) Produto - {str(err)}"
        register_log(error)


@shared_task
def task_product_inactive():
    try:

        run_products_inactive_task()

    except ValueError as err:
        error = f"(Task) Inativar Produto - {str(err)}"
        register_log(error)



@shared_task
def task_history():
    try:

        run_histories_task()

    except ValueError as err:
        error = f"(Task) Histórico - {str(err)}"
        register_log(error)


@shared_task
def task_sale():
    try:

        run_sales_task()

    except ValueError as err:
        error = f"(Task) Vendas - {str(err)}"
        register_log(error)


@shared_task
def task_order():
    try:

        run_orders_task()

    except ValueError as err:
        error = f"(Task) Pedidos - {str(err)}"
        register_log(error)


@shared_task
def task_orders_duplicate():
    try:

        run_orders_duplicate_task()

    except ValueError as err:
        error = f"(Task) Pedidos - {str(err)}"
        register_log(error)


@shared_task
def task_entry():
    try:

        run_entries_task()

    except ValueError as err:
        error = f"(Task) Entradas - {str(err)}"
        register_log(error)


@shared_task
def task_stock():
    try:

        run_stocks_task()

    except ValueError as err:
        error = f"(Task) Estoque - {str(err)}"
        register_log(error)
