from core.models import Parametros
from core.views import login_api
from core.query_oracle import ultima_entrada_db
import pandas as pd
import requests


def tratando_ultima_entrada():
    ultima_entrada_df = ultima_entrada_db()
    ultima_entrada_df.columns = ["cod_filial", "cod_produto", "desc_produto", "data", "qt_ultima_entrada"]
    ultima_entrada_df['data'] = ultima_entrada_df['data'].replace(" 00:00", "", regex=True)
    ultima_entrada = ultima_entrada_df.groupby(['data'])['qt_ultima_entrada'].sum().to_frame().reset_index()
    ultima_entrada['data'] = pd.to_datetime(ultima_entrada['data'])
    _ultima_entrada = pd.DataFrame(data=ultima_entrada)

    return _ultima_entrada


def enviar_ultima_entrada():
    dados = tratando_ultima_entrada()
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