import requests
from core.views.api_login import login_api
from core.models import Configuracao
from core.models import Registro


def get_data_business():
    qs = Configuracao.objects.get(id=1)
    return qs


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
    log_register = Registro.objects.create(message=message)
    log_register.save()
