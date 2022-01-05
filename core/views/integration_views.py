from django.http import JsonResponse
from django.shortcuts import render
from core.views.integration_routine import *
from core.views.get_data import register_log

# from core.tasks import *

def home_index(request, template_name='home.html'):
    return render(request, template_name)


def request_fornecedores(request):
    if request.is_ajax():
        # tests.delay()
        try:
            run_fornecedores(integration=True)
            msg = "Fornecedor - Sucesso ao enviar fornecedores!"
            register_log(msg)
            return JsonResponse({'data': msg})
        except ValueError as err:
            erro = f"Fornecedor - {str(err)}"
            register_log(erro)
            return JsonResponse({'data': erro})

    return JsonResponse({})


def request_produtos(request):
    if request.is_ajax():
        try:
            run_produtos(integration=True)
            msg = "Produto - Sucesso ao enviar produtos!"
            register_log(msg)
            return JsonResponse({'data': msg})
        except ValueError as err:
            erro = f"Produto - {str(err)}"
            register_log(erro)
            return JsonResponse({'data': erro})

    return JsonResponse({})


def request_historico(request):
    if request.is_ajax():
        inicio = request.POST.get('dt_inicio')
        fim = request.POST.get('dt_fim')
        try:
            run_historico(dt_inicio=inicio, dt_fim=fim, integration=True)
            msg = "Histórico - Sucesso ao enviar historico!"
            register_log(msg)
            return JsonResponse({'data': msg})
        except ValueError as err:
            erro = f"Histórico - {str(err)}"
            register_log(erro)
            return JsonResponse({'data': erro})

    return JsonResponse({})


def request_vendas(request):
    if request.is_ajax():
        inicio = request.POST.get('dt_inicio')
        fim = request.POST.get('dt_fim')
        try:
            run_vendas(dt_inicio=inicio, dt_fim=fim, integration=True)
            msg = "Vendas - Sucesso ao enviar vendas!"
            register_log(msg)
            return JsonResponse({'data': msg})
        except ValueError as err:
            erro = f"Vendas - {str(err)}"
            register_log(erro)
            return JsonResponse({'data': erro})

    return JsonResponse({})


def request_pedidos(request):
    if request.is_ajax():
        inicio = request.POST.get('dt_inicio')
        fim = request.POST.get('dt_fim')
        try:
            run_pedidos(dt_inicio=inicio, dt_fim=fim, integration=True)
            msg = "Pedidos - Sucesso ao enviar pedidos!"
            register_log(msg)
            return JsonResponse({'data': msg})
        except ValueError as err:
            erro = f"Pedidos - {str(err)}"
            register_log(erro)
            return JsonResponse({'data': erro})

    return JsonResponse({})


def request_entradas(request):
    if request.is_ajax():
        inicio = request.POST.get('dt_inicio')
        fim = request.POST.get('dt_fim')
        try:
            run_entradas(dt_inicio=inicio, dt_fim=fim, integration=True)
            msg = "Entradas - Sucesso ao enviar entradas!"
            register_log(msg)
            return JsonResponse({'data': msg})
        except ValueError as err:
            erro = f"Entradas - {str(err)}"
            register_log(erro)
            return JsonResponse({'data': erro})

    return JsonResponse({})


def request_estoque(request):
    if request.is_ajax():
        try:
            run_estoque(integration=True)
            msg = "Estoque - Sucesso ao enviar estoque!"
            register_log(msg)
            return JsonResponse({'data': msg})
        except ValueError as err:
            erro = f"Estoque - {str(err)}"
            register_log(erro)
            return JsonResponse({'data': erro})

    return JsonResponse({})
