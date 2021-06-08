from core.models import Parametros
from core.views import login_api
from core.query_oracle.query_integracao import produto_db
import pandas as pd
import requests


def tratando_produto():
    produto_df = produto_db()
    produto_df.columns = ["cod_filial", "cod_produto", "desc_produto", "data", "qt_produto"]
    produto_df['data'] = produto_df['data'].replace(" 00:00", "", regex=True)
    produto = produto_df.groupby(['data'])['qt_produto'].sum().to_frame().reset_index()
    produto['data'] = pd.to_datetime(produto['data'])
    _produto = pd.DataFrame(data=produto)

    return _produto


def enviar_produto():
    dados = tratando_produto()
    token = login_api()

    url = ''
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
