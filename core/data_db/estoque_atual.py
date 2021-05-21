from core.models import Parametros
from core.views import login_api
from core.query_oracle import estoque_atual_db
import pandas as pd
import requests


def tratando_estoque_atual():
    estoque_atual_df = estoque_atual_db()
    estoque_atual_df.columns = ["cod_filial", "cod_produto", "desc_produto", "data", "qt_estoque_atual"]
    estoque_atual_df['data'] = estoque_atual_df['data'].replace(" 00:00", "", regex=True)
    estoque_atual = estoque_atual_df.groupby(['data'])['qt_estoque_atual'].sum().to_frame().reset_index()
    estoque_atual['data'] = pd.to_datetime(estoque_atual['data'])
    _estoque_atual = pd.DataFrame(data=estoque_atual)

    return _estoque_atual


def enviar_estoque_atual():
    dados = tratando_estoque_atual()
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