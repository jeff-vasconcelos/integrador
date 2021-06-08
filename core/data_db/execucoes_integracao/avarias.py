from core.models import Parametros
from core.login_api import login_api
from core.query_oracle.query_integracao.avarias_db import avarias_db
import pandas as pd
import requests


def tratando_avarias():
    avarias_df = avarias_db()
    avarias_df.columns = ["cod_filial", "cod_produto", "desc_produto", "data", "qt_avaria"]
    avarias = avarias_df.groupby(['data', 'cod_filial', 'cod_produto', 'desc_produto'])['qt_avaria'].sum().to_frame().reset_index()
    avarias['data'] = pd.to_datetime(avarias['data'])

    avaria = pd.DataFrame(data=avarias)
    avaria['empresa'] = 1
    avaria['cod_fornecedor'] = 16

    avarias = avaria.assign(**avaria.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict("records")

    return avarias


def enviar_avarias():
    dados = tratando_avarias()
    token = login_api()

    url = "http://127.0.0.1:8000/api/avaria/"
    headers = {
        'Authorization': token
    }

    response = requests.get(url=url, headers=headers)
    print(headers)
    if response.status_code == 200:
        for i in dados:
            data = i
            response = requests.post(url=url, headers=headers, data=data)
        return response.status_code
    else:
        token = login_api()
