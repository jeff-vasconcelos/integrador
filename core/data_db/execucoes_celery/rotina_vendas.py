#from core.models import Parametros
from core.login_api import login_api
from core.query_oracle.query_celery.rotina_vendas_db import vendas_db
import pandas as pd
import requests
import datetime
import json

"""
Os dados coletados do DB, são armazenados na variável vendas_df e tratados por colunas, as colunas preco_unit e custo_fin
foram corrigidas e convertidas em float para não haver erros, assim como removi algumas das colunas onde os dados não
foram especificados.
depois as colunas foram ordenadas e a data convertida para o formato datetime
"""


def rotina_tratando_vendas():
    vendas_df = vendas_db()
    vendas_df.columns = ["cod_filial", "data", "cod_produto", "desc_produto", "qt_vendas", "preco_unit",
                                   "cliente", "peso_liquido", "cod_depto", "desc_dois", "num_nota", "cod_usur",
                                   "cod_fornecedor", "qt_unit_caixa", "cod_aux", "custo_fin", "marca",
                                   "cod_fab", "supervisor"]
    vendas_df = vendas_df.drop(columns=['cod_aux'])
    vendas_df['preco_unit'] = vendas_df['preco_unit'].replace(",", ".", regex=True).astype(float).round(3)
    vendas_df['peso_liquido'] = vendas_df['peso_liquido'].replace(",", ".", regex=True).astype(float)
    vendas_df['custo_fin'] = vendas_df['custo_fin'].replace(",", ".", regex=True).astype(float).round(3)
    vendas_df['data'] = pd.to_datetime(vendas_df['data'])

    #TODO remover depois (tem que automatizar)s
    vendas_df['empresa'] = 1

    vendas_dic = vendas_df.assign(**vendas_df.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict("records")

    return vendas_dic


def rotina_enviar_vendas():
    dados = rotina_tratando_vendas()
    token = login_api()

    url = "http://192.168.1.121/api/venda/"
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        for i in dados:
            data = json.dumps(i)
            response = requests.post(url=url, headers=headers, data=data)
        return response.status_code
    else:
        token = login_api()
