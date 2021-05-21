from core.models import Parametros
from core.views import login_api
from core.query_oracle import p_compras_db
import pandas as pd
import requests


def tratando_p_compras():
    p_compras_df = p_compras_db()
    p_compras_df.columns = ["cod_filial", "cod_produto", "desc_produto", "data", "qt_hist_estoque"]
    p_compras_df['data'] = p_compras_df['data'].replace(" 00:00", "", regex=True)
    p_compras = p_compras_df.groupby(['data'])['qt_hist_estoque'].sum().to_frame().reset_index()
    p_compras['data'] = pd.to_datetime(p_compras['data'])
    _p_compras = pd.DataFrame(data=p_compras)

    return _p_compras


def enviar_p_compras():
    dados = tratando_p_compras()
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