from core.models import Parametros
from core.login_api import login_api
from core.query_oracle.query_celery.rotina_ultima_entrada_db import ultima_entrada_db
import pandas as pd
import requests
import json


def rotina_tratando_ultima_entrada():
    ultima_entrada_df = ultima_entrada_db()
    ultima_entrada_df.columns = ["cod_filial", "cod_produto", "desc_produto", "data", "vl_ult_entrada", "qt_ult_entrada"]
    ultima_entrada_df['vl_ult_entrada'] = ultima_entrada_df['vl_ult_entrada'].replace(",", ".", regex=True).astype(float).round(3)
    ultima_entrada_df['data'] = pd.to_datetime(ultima_entrada_df['data'])
    ultima_entrada_df.fillna(0, inplace=True)

    entradas_df = ultima_entrada_df

    #TODO remover depois (tem que automatizar)
    entradas_df['empresa'] = 1
    entradas_df['cod_fornecedor'] = 16

    entradas = entradas_df.assign(**entradas_df.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict(
        "records")

    return entradas


def rotina_enviar_ultima_entrada():
    dados = rotina_tratando_ultima_entrada()
    token = login_api()

    url = "http://192.168.1.121/api/ultima-entrada/"
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
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
