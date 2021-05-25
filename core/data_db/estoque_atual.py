from core.models import Parametros
from core.login_api import login_api
from core.query_oracle.estoque_atual_db import estoque_atual_db
import pandas as pd
import requests


def tratando_estoque_atual():
    estoque_atual_df = estoque_atual_db()
    estoque_atual_df.columns = ["desc_produto", "cod_filial", "filial", "cod_produto", "cod_fornecedor", "fornecedor", "embalagem", "qt_estoque_gerado", "qt_indenizado", "custo_ultima_entrada", "qt_reserva", "qt_pendente", "qt_estoque_atual"]
    #estoque_atual_df['data'] = estoque_atual_df['data'].replace(" 00:00", "", regex=True)
    estoque_atual = estoque_atual_df.groupby(['desc_produto', 'cod_filial', 'filial', 'cod_produto', 'cod_fornecedor', 'fornecedor', 'embalagem', 'qt_estoque_gerado', 'qt_indenizado', 'custo_ultima_entrada', 'qt_reserva', 'qt_pendente'])['qt_estoque_atual'].sum().to_frame().reset_index()
    #estoque_atual['data'] = pd.to_datetime(estoque_atual['data'])
    _estoque_atual = pd.DataFrame(data=estoque_atual)
    _estoque_atual['empresa'] = 1
    _estoque_atual['cod_fornecedor'] = 16
    #estoque_atual = _estoque_atual.assign(**_estoque_atual.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict("records")

    #print(estoque_atual)

    return estoque_atual


def enviar_estoque_atual():
    dados = tratando_estoque_atual()
    token = login_api()

    url = 'http://127.0.0.1:8000/api/estoque-atual/'
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