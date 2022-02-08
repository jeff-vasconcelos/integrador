import requests
from datetime import datetime
from core.views.api_login import login_api
from django.http import HttpResponse
from core.models.providers import Provider
from core.models.products import Product


def get_providers_api(id_company):
    token = login_api()
    # results = Provider.objects.filter(company=id)

    url = f'https://insight.ecluster.com.br/api/integration/providers-company/{id_company}/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    results = requests.get(url=url, headers=headers).json()

    list_providers = []
    for i in results:
        list_providers.append(i['cod_fornecedor'])

    return list_providers


def get_products_api(id_company):

    # results = Product.objects.filter(company=id)

    token = login_api()

    url = f'https://insight.ecluster.com.br/api/integration/products-company/{id_company}/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    results = requests.get(url=url, headers=headers).json()

    list_products = []
    for i in results:
        list_products.append(i['cod_produto'])

    return list_products


def get_branches_api(id_company):
    token = login_api()

    url = f'https://insight.ecluster.com.br/api/integration/branches-company/{id_company}/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    results = requests.get(url=url, headers=headers).json()

    list_branches = []
    for i in results:
        list_branches.append(i['cod_filial'])

    return list_branches


def get_orders_api(id_company):
    token = login_api()

    url = f'https://insight.ecluster.com.br/api/integration/orders-company/{id_company}/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    results = requests.get(url=url, headers=headers).json()

    list_orders = []
    for i in results:
        list_orders.append({"num_pedido": i['num_pedido'], "cod_produto": i['cod_produto']})

    # result = remove_repete(list_orders)

    return list_orders


def get_stock_api(id_company):
    token = login_api()

    url = f'https://insight.ecluster.com.br/api/integration/stock-company/{id_company}/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    results = requests.get(url=url, headers=headers).json()

    list_stock_products = []

    for i in results:
        list_stock_products.append(
            {
                "cod_produto": i['cod_produto'],
                "cod_filial": i['cod_filial'],
                "qt_geral": i['qt_geral'],
                "qt_disponivel": i['qt_disponivel'],
                "preco_venda": i['preco_venda']

            }
        )

    return list_stock_products


def remove_repete(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l


def register_log(message):
    
    message_date = f"{datetime.now()} {message}"
    
    f = open('log.txt', 'a', encoding='utf-8')
    f.write(message_date)
    f.write('\n')
    f.close()

