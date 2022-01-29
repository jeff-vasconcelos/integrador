import requests
import datetime
from core.views.api_login import login_api
from django.http import HttpResponse


def get_providers_api(id):
    token = login_api()

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


def get_orders_api(id):
    token = login_api()

    url = f'https://insight.ecluster.com.br/api/integration/orders-company/{id}/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    results = requests.get(url=url, headers=headers).json()

    list_orders = []
    for i in results:
        list_orders.append(i['num_pedido'])

    result = remove_repete(list_orders)

    return result

def remove_repete(lista):
    l = []
    for i in lista:
        if i not in l:
            l.append(i)
    l.sort()
    return l


def register_log(message):
    
    message_date = f"{datetime.datetime.now()} {message}"
    
    f = open('log.txt', 'a', encoding='utf-8')
    f.write(message_date)
    f.write('\n')
    f.close()

