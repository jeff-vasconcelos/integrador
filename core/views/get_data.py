import requests
import datetime
from core.views.api_login import login_api
from core.models import Registro
from django.http import HttpResponse


def get_fornecedores_api(id):
    token = login_api()

    url = f'https://insight.ecluster.com.br/api/integration/fornecedor/empresa/{id}/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    resultado = requests.get(url=url, headers=headers).json()

    lista_fornecedores = []
    for i in resultado:
        lista_fornecedores.append(i['cod_fornecedor'])

    return lista_fornecedores


def get_produtos_api(id):
    token = login_api()

    url = f'https://insight.ecluster.com.br/api/integration/produto/empresa/{id}/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    resultado = requests.get(url=url, headers=headers).json()

    lista_produtos = []
    for i in resultado:
        lista_produtos.append(i['cod_produto'])

    return lista_produtos


def get_filial_api(id):
    token = login_api()

    url = f'https://insight.ecluster.com.br/api/integration/filial/empresa/{id}/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    resultado = requests.get(url=url, headers=headers).json()

    lista_filial = []
    for i in resultado:
        lista_filial.append(i['cod_filial'])

    return lista_filial


def register_log(message):
    
    message_date = f"{datetime.datetime.now()} {message}"
    
    f = open('log.txt', 'a', encoding='utf-8')
    f.write(message_date)
    f.write('\n')
    f.close()
    
    #log_register = Registro.objects.create(message=message)
    #log_register.save()
