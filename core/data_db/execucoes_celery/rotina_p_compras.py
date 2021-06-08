from core.models import Parametros
from core.login_api import login_api
from core.query_oracle.query_celery.rotina_p_compras_db import p_compras_db
import pandas as pd
import requests


def rotina_tratando_p_compras():
    p_compras_df = p_compras_db()
    p_compras_df.columns = ["cod_filial", "cod_produto", "desc_produto", "saldo", "num_pedido", "data"]
    p_compras = p_compras_df.groupby(['data', "cod_filial", "cod_produto", "desc_produto", "saldo"])['num_pedido'].sum().to_frame().reset_index()
    p_compras['data'] = pd.to_datetime(p_compras['data'])

    _p_compras = pd.DataFrame(data=p_compras)
    _p_compras['empresa'] = 1
    _p_compras['cod_fornecedor'] = 16

    p_compras = _p_compras.assign(**_p_compras.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict("records")

    return p_compras


def rotina_enviar_p_compras():
    dados = rotina_tratando_p_compras()
    token = login_api()

    url = 'http://127.0.0.1:8000/api/pedido-compra/'
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
