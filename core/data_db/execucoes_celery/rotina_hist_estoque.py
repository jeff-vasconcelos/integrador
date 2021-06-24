from core.models import Parametros
from core.login_api import login_api
from core.query_oracle.query_celery.rotina_hist_estoque_db import hist_estoque_db
import pandas as pd
import requests
import datetime
import json


def rotina_tratando_hist_estoque():
    hist_estoque_df = hist_estoque_db()
    hist_estoque_df.columns = ["cod_filial", "cod_produto", "desc_produto", "embalagem", "data", "qt_estoque"]
    hist_estoque_df['data'] = pd.to_datetime(hist_estoque_df['data'])
    hist_estoque_df.fillna(0, inplace=True)

    historico_df = hist_estoque_df

    # TODO remover depois (tem que automatizar)
    historico_df['empresa'] = 1
    historico_df['cod_fornecedor'] = 16

    historico = historico_df.assign(**historico_df.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict(
        "records")

    return historico


def rotina_enviar_hist_estoque():
    dados = rotina_tratando_hist_estoque()
    token = login_api()

    url = 'http://192.168.1.121/api/historico-estoque/'
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
