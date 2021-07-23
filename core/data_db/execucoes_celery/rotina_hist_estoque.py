from core.login_api import login_api
from core.query import query_hist
import pandas as pd
import requests
import json


def rotina_tratando_hist_estoque():
    hist_estoque_df = query_hist()
    hist_estoque_df.columns = ["cod_produto", "data", "qt_estoque", "cod_filial", "cod_fornecedor"]
    hist_estoque_df['qt_estoque'] = hist_estoque_df['qt_estoque'].replace(",", ".", regex=True).astype(int).round(3)
    hist_estoque_df['data'] = pd.to_datetime(hist_estoque_df['data'])
    hist_estoque_df.fillna(0, inplace=True)

    historico_df = hist_estoque_df

    # TODO remover depois (tem que automatizar)
    historico_df['empresa'] = 1
    historico_df = historico_df.query('cod_fornecedor==267')

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
