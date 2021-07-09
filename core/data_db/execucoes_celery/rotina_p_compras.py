from core.models import Parametros
from core.login_api import login_api
from core.query import query_p_compras
import pandas as pd
import requests
import datetime
import json


def rotina_tratando_p_compras():
    df_pedidos_compras = query_p_compras()
    df_pedidos_compras.columns = ["cod_filial", "cod_produto", "desc_produto", "saldo", "num_pedido", "data"]
    df_pedidos_compras['data'] = pd.to_datetime(df_pedidos_compras['data'])
    df_pedidos_compras.fillna(0, inplace=True)

    pedidos_df = df_pedidos_compras

    # TODO remover depois (tem que automatizar)
    pedidos_df['empresa'] = 1
    pedidos_df['cod_fornecedor'] = 16


    p_compras = pedidos_df.assign(**pedidos_df.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict("records")

    return p_compras


def rotina_enviar_p_compras():
    dados = rotina_tratando_p_compras()
    token = login_api()

    url = 'http://192.168.1.121/api/pedido-compra/'
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
