from core.models import Parametros
from core.login_api import login_api
from core.query_oracle.ultima_entrada_db import ultima_entrada_db
import pandas as pd
import requests


def tratando_ultima_entrada():
    ultima_entrada_df = ultima_entrada_db()
    ultima_entrada_df.columns = ["desc_produto", "cod_filial", "filial", "cod_produto", "data", "valor_ultima_entrada", "qt_ultima_entrada"]
    #ultima_entrada_df['data'] = ultima_entrada_df['data'].replace(" 00:00", "", regex=True)
    ultima_entrada = ultima_entrada_df.groupby(['data', "desc_produto", "cod_filial", "filial", "cod_produto", "valor_ultima_entrada"])['qt_ultima_entrada'].sum().to_frame().reset_index()
    ultima_entrada['data'] = pd.to_datetime(ultima_entrada['data'])
    _ultima_entrada = pd.DataFrame(data=ultima_entrada)
    _ultima_entrada['empresa'] = 1
    _ultima_entrada['cod_fornecedor'] = 16
    ultima_entrada = ultima_entrada.assign(**ultima_entrada.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict("records")

    return ultima_entrada


def enviar_ultima_entrada():
    dados = tratando_ultima_entrada()
    token = login_api()

    url = 'http://127.0.0.1:8000/api/ultima-entrada/'
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