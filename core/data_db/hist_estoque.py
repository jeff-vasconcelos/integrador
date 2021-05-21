from core.models import Parametros
from core.views import login_api
from core.query_oracle import hist_estoque_db
import pandas as pd
import requests


def tratando_hist_estoque():
    hist_estoque_df = hist_estoque_db()
    hist_estoque_df.columns = ["cod_filial", "cod_produto", "desc_produto", "data", "qt_hist_estoque"]
    hist_estoque_df['data'] = hist_estoque_df['data'].replace(" 00:00", "", regex=True)
    hist_estoque = hist_estoque_df.groupby(['data'])['qt_hist_estoque'].sum().to_frame().reset_index()
    hist_estoque['data'] = pd.to_datetime(hist_estoque['data'])
    _hist_estoque = pd.DataFrame(data=hist_estoque)

    return _hist_estoque


def enviar_hist_estoque():
    dados = tratando_hist_estoque()
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