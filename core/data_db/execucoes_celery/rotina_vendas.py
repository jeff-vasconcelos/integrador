#from core.models import Parametros
from core.login_api import login_api
from core.query_oracle.query_celery.rotina_vendas_db import vendas_db
import pandas as pd
import requests

"""
Os dados coletados do DB, são armazenados na variável vendas_df e tratados por colunas, as colunas preco_unit e custo_fin
foram corrigidas e convertidas em float para não haver erros, assim como removi algumas das colunas onde os dados não
foram especificados.
depois as colunas foram ordenadas e a data convertida para o formato datetime
"""


def rotina_tratando_vendas():
    vendas_df = vendas_db()
    vendas_df.columns = ["data", "desc_produto", "cod_filial", "filial", "qt_vendas", "cod_produto", "preco_unit", "desc_produto2", "codepto","cod_fornecedor", "qtd_unid_cx", "custo_fin", "marca", "peso_liq", "cod_fab"]
    vendas_df['preco_unit'] = vendas_df['preco_unit'].replace(",", ".", regex=True)
    vendas_df['preco_unit'] = vendas_df['preco_unit'].astype(float)
    vendas_df['custo_fin'] = vendas_df['custo_fin'].replace(",", ".", regex=True)
    vendas_df['custo_fin'] = vendas_df['custo_fin'].astype(float)
    vendas_df = vendas_df.drop(columns=["filial", "desc_produto2", "codepto", "qtd_unid_cx", "marca", "peso_liq", "cod_fab"])

    vendas = vendas_df.groupby(['data', 'cod_produto', 'desc_produto', 'cod_filial', 'cod_fornecedor', 'preco_unit', 'custo_fin'])['qt_vendas'].sum().to_frame().reset_index()
    vendas['data'] = pd.to_datetime(vendas['data'])

    _vendas = pd.DataFrame(data=vendas)
    _vendas['empresa'] = 1
    _vendas['cod_fornecedor'] = 16

    vendas = _vendas.assign(**_vendas.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict("records")

    return vendas


def rotina_enviar_vendas():
    dados = rotina_tratando_vendas()
    token = login_api()

    url = "http://127.0.0.1:8000/api/venda/"
    headers = {
        'Authorization': token
    }

    response = requests.get(url=url, headers=headers)
    print(headers)

    if response.status_code == 200:
        for i in dados:
            data = i
            response = requests.post(url=url, headers=headers, data=data)
        return response.status_code
    else:
        token = login_api()
