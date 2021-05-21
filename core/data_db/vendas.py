from core.models import Parametros
from core.views import login_api
from core.query_oracle import vendas_db
import pandas as pd
import requests


def tratando_vendas():
    vendas_df = vendas_db()
    vendas_df.columns = ["cod_filial", "cod_produto", "desc_produto", "data", "qt_vendas"]
    vendas_df['data'] = vendas_df['data'].replace(" 00:00", "", regex=True)
    vendas = vendas_df.groupby(['data'])['qt_vendas'].sum().to_frame().reset_index()
    vendas['data'] = pd.to_datetime(vendas['data'])
    _vendas = pd.DataFrame(data=vendas)

    return _vendas


def enviar_vendas():
    dados = tratando_vendas()
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