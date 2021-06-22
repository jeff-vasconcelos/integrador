from core.models import Parametros
from core.login_api import login_api
from core.query_oracle.query_celery.rotina_estoque_atual_db import estoque_atual_db
import pandas as pd
import requests

"""
Os dados coletados do DB, são armazenados na variável estoque_atual_df e tratados por colunas, a coluna custo_ult_ent
foi corrigida e convertida em float para não haver erros, assim como removi algumas das colunas onde os dados não
foram especificadas.
os valores NA foram preenchidos com o valor:0.
Depois as colunas foram ordenadas e a data convertida para o formato datetime
"""


def rotina_tratando_estoque_atual():
    estoque_atual_df = estoque_atual_db()
    estoque_atual_df.columns = ["desc_produto", "cod_filial", "filial", "cod_produto", "cod_fornecedor", "fornecedor", "embalagem", "qt_estoque_geral", "qt_indenizada", "custo_ult_ent", "qt_reservada", "qt_pendente", "qt_disponivel"]
    estoque_atual_df.drop(columns=['fornecedor', 'filial'], inplace=True)
    estoque_atual_df['custo_ult_ent'] = estoque_atual_df['custo_ult_ent'].replace(",", ".", regex=True)
    estoque_atual_df['custo_ult_ent'] = estoque_atual_df['custo_ult_ent'].astype(float)
    values = {'qt_estoque_geral': 0}
    estoque_atual_df.fillna(value=values, inplace=True)
    estoque_atual = estoque_atual_df.groupby(['desc_produto', 'cod_filial', 'cod_produto', 'cod_fornecedor', 'embalagem', 'qt_estoque_geral', 'qt_indenizada', 'custo_ult_ent', 'qt_reservada', 'qt_pendente'])['qt_disponivel'].sum().to_frame().reset_index()

    _estoque_atual = pd.DataFrame(data=estoque_atual)
    _estoque_atual['empresa'] = 1
    _estoque_atual['cod_fornecedor'] = 16
    _estoque_atual['data'] = '2021-05-27'

    estoque_atual = _estoque_atual.assign(**_estoque_atual.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict("records")

    return estoque_atual


def rotina_enviar_estoque_atual():
    dados = rotina_tratando_estoque_atual()
    token = login_api()

    url = 'http://192.168.1.121/api/estoque-atual/'
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
