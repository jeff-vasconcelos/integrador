from core.login_api import login_api
from core.query import query_estoque
import pandas as pd
import requests
import datetime
import json


def rotina_tratando_estoque_atual():
    estoque_atual_df = query_estoque()

    estoque_atual_df.columns = ["desc_produto", "embalagem", "cod_filial", "cod_produto", "qt_estoque_geral", "qt_indenizada", "qt_reservada", "qt_pendente", "qt_bloqueada", "qt_disponivel", "custo_ult_ent", "cod_fornecedor",  "fornecedor", "preco_venda"]

    estoque_atual_df['qt_disponivel'] = estoque_atual_df['qt_disponivel'].replace(",", ".", regex=True).astype(int)
    estoque_atual_df['qt_estoque_geral'] = estoque_atual_df['qt_estoque_geral'].replace(",", ".", regex=True).astype(int)
    estoque_atual_df['custo_ult_ent'] = estoque_atual_df['custo_ult_ent'].replace(",", ".", regex=True).astype(float).round(3)
    estoque_atual_df['preco_venda'] = estoque_atual_df['preco_venda'].replace(",", ".", regex=True).astype(float).round(3)
    estoque_atual_df = estoque_atual_df.drop(columns=['fornecedor'])
    estoque_atual_df['data'] = datetime.date.today()
    estoque_atual_df['data'] = pd.to_datetime(estoque_atual_df['data'])

    #TODO remover depois (Tem que automatizar)
    estoque_atual_df['empresa'] = 1

    estoque_atual = estoque_atual_df.assign(**estoque_atual_df.select_dtypes(["datetime"]).astype(str).to_dict("list")
                                            ).to_dict("records")

    return estoque_atual


def rotina_enviar_estoque_atual():
    dados = rotina_tratando_estoque_atual()
    token = login_api()

    url = 'http://192.168.1.121/api/estoque-atual/'
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'dataType': 'json',
        'Accept': 'application/json'
    }

    response = requests.get(url=url, headers=headers)
    print(headers)

    if response.status_code == 200:
        for i in dados:
            data = json.dumps(i)
            response = requests.post(url=url, headers=headers, data=data)
        return response.status_code
    else:
        token = login_api()
