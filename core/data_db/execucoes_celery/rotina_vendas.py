from core.login_api import login_api
from core.query import query_p_vendas
import pandas as pd
import requests
import json


def rotina_tratando_vendas():
    vendas_df = query_p_vendas()
    if vendas_df.empty:
        print("VAZIO ATÉ ENTÃO!!!")
        retorno = {}
        return retorno
    else:
        vendas_df.columns = ["data", "cod_produto", "qt_venda", "preco_unit", "cod_filial", "cliente", "num_nota", "rca","cod_fornecedor", "custo_fin", "supervisor"]
        vendas_df['data'] = pd.to_datetime(vendas_df['data'])

        #TODO remover depois (tem que automatizar)
        vendas_df['empresa'] = 5

        vendas_dic = vendas_df.assign(**vendas_df.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict("records")

        return vendas_dic


def rotina_enviar_vendas():
    dados = rotina_tratando_vendas()
    token = login_api()

    url = 'https://insight.ecluster.com.br/api/venda/'

    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    url2 = 'https://insight.ecluster.com.br/api/integration/'
    response = requests.get(url=url2, headers=headers)

    if response.status_code == 200:
        for i in dados:
            data = json.dumps(i)
            response = requests.post(url=url, headers=headers, data=data)
        return response.status_code
    else:
        token = login_api()
