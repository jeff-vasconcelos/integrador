from core.login_api import login_api
from core.query import query_p_vendas
import pandas as pd
import requests
import json


def rotina_tratando_vendas():
    vendas_df = query_p_vendas()
    vendas_df.columns = ["data", "cod_produto",  "desc_produto", "qt_vendas", "preco_unit", "cod_filial",
                                 "cliente", "peso_liquido", "cod_depto", "desc_dept", "num_nota", "cod_usur",
                                 "cod_fornecedor", "secao", "qt_unit_caixa", "cod_aux", "custo_fin", "marca",
                                 "cod_fab", "supervisor"]

    vendas_df['preco_unit'] = vendas_df['preco_unit'].replace(",", ".", regex=True).astype(float).round(3)
    vendas_df['peso_liquido'] = vendas_df['peso_liquido'].replace(",", ".", regex=True).astype(float)
    vendas_df['custo_fin'] = vendas_df['custo_fin'].replace(",", ".", regex=True).astype(float).round(3)
    vendas_df['data'] = pd.to_datetime(vendas_df['data'])

    #TODO remover depois (tem que automatizar)
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
