import requests
import json
from core.views.get_data import register_log


def send_data_integration(url, token, lista_dados):
    len_lista = len(lista_dados)

    if len_lista > 20:
        n = int(round(len(lista_dados) / 20, 0))
    else:
        n = 1

    dados = [lista_dados[i::n] for i in range(n)]

    send_data(url, token, dados)


def send_data_tasks(url, token, lista_dados):
    send_data(url, token, lista_dados)


def send_data(url, token, dados):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    try:
        for i in dados:
            data = json.dumps(i)
            response = requests.post(url=url, headers=headers, data=data)
            print(response)

    except requests.exceptions.RequestException as e:  # This is the correct syntax
        register_log('Erro: function(send_data) - Nao foi possivel conectar ao servidor')
        raise SystemExit(e)


def send_data_tasks_delete(url, token, lista_dados):
    send_data_delete(url, token, lista_dados)


def send_data_delete(url, token, dados):
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    try:
        for i in dados:
            data = json.dumps(i)

            response = requests.post(url=url, headers=headers, data=data)
            print(response)

    except requests.exceptions.RequestException as e:  # This is the correct syntax
        register_log('Erro: function(send_data) - Nao foi possivel conectar ao servidor')
        raise SystemExit(e)
