from core.models import Parametros
from core.login_api import login_api
from core.query_oracle.query_celery.rotina_produto_db import produtos_db
import pandas as pd
import requests
import datetime
import json


def rotina_tratando_produto():
    df_produtos = produtos_db()
    df_produtos.columns = ["cod_produto", "desc_produto", "embalagem", "quantidade_un_cx", "marca", "peso_liq",
                          "cod_fornecedor"]

    df_produtos['empresa'] = 1

    df_produtos['quantidade_un_cx'] = df_produtos['quantidade_un_cx'].replace(",", ".", regex=True).astype(float).round(3)
    produtos_dic = df_produtos.assign(**df_produtos.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict(
        "records")

    return produtos_dic


def rotina_enviar_produto():
    dados = rotina_tratando_produto()
    token = login_api()

    url = 'http://192.168.1.121/api/produto/'
    headers = {
        'Authorization': token,
        'content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    response = requests.get(url=url, headers=headers)
    print(headers)

    if response.status_code == 200:
        for i in dados:
            data = json.dumps(i)
            response = requests.post(url=url, headers=headers, data=data)
        return response.status_code
    else:
        token = login_api()