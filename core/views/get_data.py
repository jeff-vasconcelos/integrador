import requests
from decouple import config
from datetime import datetime
from core.views.api_login import login_api


def get_providers_api(id_company):
    token = login_api()

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    results = requests.get(url=f"{config('URL_INSIGHT_GET_PROVIDERS')}{id_company}/",
                           headers=headers).json()

    list_providers = []
    for i in results:
        list_providers.append(int(i['cod_fornecedor']))

    return list_providers


def get_products_api(id_company):

    token = login_api()

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    results = requests.get(url=f"{config('URL_INSIGHT_GET_PRODUCT')}{id_company}/",
                           headers=headers).json()

    list_products = []
    for i in results:
        list_products.append(int(i['cod_produto']))

    return list_products


def get_branches_api(id_company):
    token = login_api()

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    results = requests.get(url=f"{config('URL_INSIGHT_GET_BRANCHES')}{id_company}/",
                           headers=headers).json()

    list_branches = []
    for i in results:
        list_branches.append(int(i['cod_filial']))

    return list_branches


def get_orders_api(id_company):
    token = login_api()

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    results = requests.get(url=f"{config('URL_INSIGHT_GET_ORDERS')}{id_company}/",
                           headers=headers).json()

    list_orders = []
    for i in results:
        list_orders.append({"num_pedido": int(i['num_pedido']), "cod_produto": int(i['cod_produto'])})

    return list_orders


def register_log(message):
    
    message_date = f"{datetime.now()} {message}"
    
    f = open('log.txt', 'a', encoding='utf-8')
    f.write(message_date)
    f.write('\n')
    f.close()

