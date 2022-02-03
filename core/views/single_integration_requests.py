from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from core.views.get_data import register_log
from core.views.single_integration import (run_providers_single, run_products_single, run_histories_single,
                                           run_sales_single, run_orders_single, run_entries_single, run_stocks_single)


@login_required()
def home_index(request, template_name='home.html'):
    return render(request, template_name)


def request_providers(request):
    if request.is_ajax():
        try:
            run_providers_single()
            msg = "Fornecedor - Sucesso ao enviar fornecedores!"
            register_log(msg)
            return JsonResponse({'data': msg})

        except ValueError as err:
            error = f"Fornecedor - {str(err)}"
            register_log(error)
            return JsonResponse({'data': error})

    return JsonResponse({})


def request_products(request):
    if request.is_ajax():
        try:
            run_products_single()
            msg = "Produto - Sucesso ao enviar produtos!"
            register_log(msg)
            return JsonResponse({'data': msg})

        except ValueError as err:
            error = f"Produto - {str(err)}"
            register_log(error)
            return JsonResponse({'data': error})

    return JsonResponse({})


def request_histories(request):
    if request.is_ajax():

        start = request.POST.get('dt_inicio')
        end = request.POST.get('dt_fim')

        try:
            run_histories_single(date_start=start, date_end=end)
            msg = "Histórico - Sucesso ao enviar historico!"
            register_log(msg)
            return JsonResponse({'data': msg})

        except ValueError as err:
            error = f"Histórico - {str(err)}"
            register_log(error)
            return JsonResponse({'data': error})

    return JsonResponse({})


def request_sales(request):
    if request.is_ajax():

        start = request.POST.get('dt_inicio')
        end = request.POST.get('dt_fim')

        try:
            run_sales_single(date_start=start, date_end=end)
            msg = "Vendas - Sucesso ao enviar vendas!"
            register_log(msg)
            return JsonResponse({'data': msg})

        except ValueError as err:
            error = f"Vendas - {str(err)}"
            register_log(error)
            return JsonResponse({'data': error})

    return JsonResponse({})


def request_orders(request):
    if request.is_ajax():

        start = request.POST.get('dt_inicio')
        end = request.POST.get('dt_fim')

        try:
            run_orders_single(date_start=start, date_end=end)
            msg = "Pedidos - Sucesso ao enviar pedidos!"
            register_log(msg)
            return JsonResponse({'data': msg})

        except ValueError as err:
            error = f"Pedidos - {str(err)}"
            register_log(error)
            return JsonResponse({'data': error})

    return JsonResponse({})


def request_entries(request):
    if request.is_ajax():

        start = request.POST.get('dt_inicio')
        end = request.POST.get('dt_fim')

        try:
            run_entries_single(date_start=start, date_end=end)
            msg = "Entradas - Sucesso ao enviar entradas!"
            register_log(msg)
            return JsonResponse({'data': msg})

        except ValueError as err:
            error = f"Entradas - {str(err)}"
            register_log(error)
            return JsonResponse({'data': error})

    return JsonResponse({})


def request_stock(request):
    if request.is_ajax():
        try:
            run_stocks_single()
            msg = "Estoque - Sucesso ao enviar estoque!"
            register_log(msg)
            return JsonResponse({'data': msg})

        except ValueError as err:
            error = f"Estoque - {str(err)}"
            register_log(error)
            return JsonResponse({'data': error})

    return JsonResponse({})
