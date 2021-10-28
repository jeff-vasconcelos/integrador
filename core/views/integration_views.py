from django.http import JsonResponse
from django.shortcuts import render
from core.views.integration_routine import *
from core.views.get_data import register_log


def home_index(request, template_name='home.html'):
    return render(request, template_name)


def request_fornecedores(request):
    if request.is_ajax():
        try:
            run_fornecedores(integration=True)
            msg = "Success: Integração - Fornecedores enviados com sucesso!"
            register_log(msg)
            return JsonResponse({'data': msg})
        except NameError as err:
            erro = str(err)
            register_log(f"Error : {erro}")
            return JsonResponse({'data': erro})

    return JsonResponse({})


def request_produtos(request):
    if request.is_ajax():
        try:
            run_produtos(integration=True)
            msg = "Success: Integração - Produtos enviados com sucesso!"
            register_log(msg)
            return JsonResponse({'data': msg})
        except NameError as err:
            erro = str(err)
            register_log(f"Error : {erro}")
            return JsonResponse({'data': erro})

    return JsonResponse({})


def request_historico(request):
    if request.is_ajax():
        inicio = request.POST.get('dt_inicio')
        fim = request.POST.get('dt_fim')
        try:
            run_historico(dt_inicio=inicio, dt_fim=fim, integration=True)
            msg = "Success: Integração - Histórico enviado com sucesso!"
            register_log(msg)
            return JsonResponse({'data': msg})
        except NameError as err:
            erro = str(err)
            register_log(f"Error : {erro}")
            return JsonResponse({'data': erro})

    return JsonResponse({})


def request_vendas(request):
    if request.is_ajax():
        inicio = request.POST.get('dt_inicio')
        fim = request.POST.get('dt_fim')
        try:
            run_vendas(dt_inicio=inicio, dt_fim=fim, integration=True)
            msg = "Success: Integração - Vendas enviadas com sucesso!"
            register_log(msg)
            return JsonResponse({'data': msg})
        except NameError as err:
            erro = str(err)
            register_log(f"Error : {erro}")
            return JsonResponse({'data': erro})

    return JsonResponse({})


def request_pedidos(request):
    if request.is_ajax():
        inicio = request.POST.get('dt_inicio')
        fim = request.POST.get('dt_fim')
        try:
            run_pedidos(dt_inicio=inicio, dt_fim=fim, integration=True)
            msg = "Success: Integração - Pedidos enviados com sucesso!"
            register_log(msg)
            return JsonResponse({'data': msg})
        except NameError as err:
            erro = str(err)
            register_log(f"Error : {erro}")
            return JsonResponse({'data': erro})

    return JsonResponse({})


def request_entradas(request):
    if request.is_ajax():
        inicio = request.POST.get('dt_inicio')
        fim = request.POST.get('dt_fim')
        try:
            run_entradas(dt_inicio=inicio, dt_fim=fim, integration=True)
            msg = "Success: Integração - Entradas enviadas com sucesso!"
            register_log(msg)
            return JsonResponse({'data': msg})
        except NameError as err:
            erro = str(err)
            register_log(f"Error : {erro}")
            return JsonResponse({'data': erro})

    return JsonResponse({})


def request_estoque(request):
    if request.is_ajax():
        try:
            run_estoque(integration=True)
            msg = "Success: Integração - Estoque enviado com sucesso!"
            register_log(msg)
            return JsonResponse({'data': msg})
        except NameError as err:
            erro = str(err)
            register_log(f"Error : {erro}")
            return JsonResponse({'data': erro})

    return JsonResponse({})
