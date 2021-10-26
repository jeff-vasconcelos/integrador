import requests
import json
import time
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

    url_valid_test = 'https://insight.ecluster.com.br/api/integration/'
    response = requests.get(url=url_valid_test, headers=headers)

    if response.status_code == 200:
        for i in dados:
            data = json.dumps(i)

            try:
                response = requests.post(url=url, headers=headers, data=data)

            except requests.ConnectionError:
                register_log('Error: Falha na conexão, reconectando em 150 segundos')
                time.sleep(150)
                response = requests.post(url=url, headers=headers, data=data)

        return response.status_code
    else:
        register_log('Error: Não foi possivel conectar ao servidor')
