from core.models import Parametros
from core.login_api import login_api
from core.query_oracle.vendas_db import vendas_db
import pandas as pd
import requests


def tratando_vendas():
    vendas_df = vendas_db()
    vendas_df.columns = ["data", "desc_produto", "cod_filial", "filial", "qt_vendas", "cod_produto", "preco_unit", "desc_produto2", "codepto","cod_fornecedor", "qtd_unid_cx", "custo_fin", "marca", "peso_liq", "cod_fab"]
    #vendas_df['data'] = vendas_df['data'].replace(" 00:00", "", regex=True)
    # Aqui eu removi as colunas que não serão usadas
    vendas_df.drop(columns=["filial", "desc_produto2", "codepto", "qtd_unid_cx", "marca", "peso_liq", "cod_fab"])
    vendas = vendas_df.groupby(['data', "cod_filial", "cod_produto", "preco_unit", "cod_fornecedor", "custo_fin"])['qt_vendas'].sum().to_frame().reset_index()
    vendas['data'] = pd.to_datetime(vendas['data'])
    _vendas = pd.DataFrame(data=vendas)
    _vendas['empresa'] = 1
    _vendas['cod_fornecedor'] = 16
    vendas = vendas.assign(**vendas.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict("records")

    return vendas


def enviar_vendas():
    dados = tratando_vendas()
    token = login_api()

    url = 'http://127.0.0.1:8000/api/venda/'
    headers = {
        'Authorization': token
    }

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        for i in dados:
            data = i
            response = requests.post(url=url, headers=headers, data=data)
        return response.status_code
    else:
        token = login_api()