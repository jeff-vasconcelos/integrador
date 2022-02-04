import requests
from datetime import datetime
from core.views.api_login import login_api
from django.http import HttpResponse
from core.models.providers import Provider
from core.models.products import Product


def get_providers_api(id):
    token = login_api()
    # results = Provider.objects.filter(company=id)

    url = f'https://insight.ecluster.com.br/api/integration/providers-company/{id}/'
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


def get_products_api(id):

    # results = Product.objects.filter(company=id)

    token = login_api()

    url = f'https://insight.ecluster.com.br/api/integration/products-company/{id}/'
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


def get_branches_api(id):
    token = login_api()

    url = f'https://insight.ecluster.com.br/api/integration/branches-company/{id}/'
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


def get_orders_api(id, is_duplicated=''):
    token = login_api()

    url = f'https://insight.ecluster.com.br/api/integration/orders-company/{id}/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    results = requests.get(url=url, headers=headers).json()

    if not is_duplicated:
        list_orders = []
        list_orders_products = []
        list_orders_branches = []
        list_orders_quantity_over = []
        # list_orders_date = []

        for i in results:
            list_orders.append(i['num_pedido'])
            list_orders_products.append(i['cod_produto'])
            list_orders_branches.append(i['cod_filial'])
            list_orders_quantity_over.append(i['saldo'])
            # list_orders_date.append(datetime.strptime(i['data'], '%Y/%m/%d').date())

        return list_orders, list_orders_products, list_orders_branches, list_orders_quantity_over

    list_orders = []
    for i in results:
        list_orders.append(i['num_pedido'])

    result = remove_repete(list_orders)

    return result


def get_stock_api(id):
    token = login_api()

    url = f'https://insight.ecluster.com.br/api/integration/stock-company/{id}/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    results = requests.get(url=url, headers=headers).json()

    list_stock_produto = []
    list_stock_filial = []
    list_stock_qt_geral = []
    list_stock_qt_disponivel = []

    list_stock_preco = []
    for i in results:
        list_stock_produto.append(i['cod_produto'])
        list_stock_filial.append(i['cod_filial'])
        list_stock_qt_geral.append(i['qt_geral'])
        list_stock_qt_disponivel.append(i['qt_disponivel'])
        # list_stock_data.append(i['data'])
        # list_stock_data.append(datetime.strptime(i['data'], '%Y/%m/%d').date())
        list_stock_preco.append(i['preco_venda'])

    # result = remove_repete(list_stock)

    return list_stock_produto, list_stock_filial, list_stock_qt_geral, list_stock_qt_disponivel, list_stock_preco


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

