from core.models import Parametros
from core.views import login_api
from core.query_oracle import avarias_db
import pandas as pd
import requests


def tratando_avarias():
    avarias_df = avarias_db()
    avarias_df.columns = ["cod_filial", "cod_produto", "desc_produto", "data", "qt_avaria"]
    avarias_df['data'] = avarias_df['data'].replace(" 00:00", "", regex=True)
    avarias = avarias_df.groupby(['data'])['qt_avaria'].sum().to_frame().reset_index()
    avarias['data'] = pd.to_datetime(avarias['data'])
    avaria = pd.DataFrame(data=avarias)

    return avaria


def enviar_avarias():
    dados = tratando_avarias()
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