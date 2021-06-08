from core.models import Parametros
from core.views import login_api
from core.query_oracle.query_celery import fornecedor_db
import pandas as pd
import requests


def rotina_tratando_fornecedor():
    fornecedor_df = fornecedor_db()
    fornecedor_df.columns = ["cod_filial", "cod_produto", "desc_produto", "data", "qt_fornecedor"]
    fornecedor_df['data'] = fornecedor_df['data'].replace(" 00:00", "", regex=True)
    fornecedor = fornecedor_df.groupby(['data'])['qt_fornecedor'].sum().to_frame().reset_index()
    fornecedor['data'] = pd.to_datetime(fornecedor['data'])
    _fornecedor = pd.DataFrame(data=fornecedor)

    return _fornecedor


def rotina_enviar_fornecedor():
    dados = rotina_tratando_fornecedor()
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
