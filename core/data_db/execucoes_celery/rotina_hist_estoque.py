from core.models import Parametros
from core.login_api import login_api
from core.query_oracle.query_celery.rotina_hist_estoque_db import hist_estoque_db
import pandas as pd
import requests


def rotina_tratando_hist_estoque():
    hist_estoque_df = hist_estoque_db()
    hist_estoque_df.columns = ["cod_filial", "filial", "cod_produto", "data", "desc_produto", "embalagem", "qt_estoque_geral"]
    hist_estoque = hist_estoque_df.groupby(['data', "cod_filial", "filial", "cod_produto", "desc_produto", "embalagem"])['qt_estoque_geral'].sum().to_frame().reset_index()
    hist_estoque['data'] = pd.to_datetime(hist_estoque['data'])

    _hist_estoque = pd.DataFrame(data=hist_estoque)
    _hist_estoque['empresa'] = 1
    _hist_estoque['cod_fornecedor'] = 16

    hist_estoque = _hist_estoque.assign(**_hist_estoque.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict("records")

    return hist_estoque


def rotina_enviar_hist_estoque():
    dados = rotina_tratando_hist_estoque()
    token = login_api()

    url = 'http://127.0.0.1:8000/api/historico-estoque/'
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
