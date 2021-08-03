from core.login_api import login_api
from core.query import query_fornecedor
import requests


def rotina_tratando_fornecedor():
    fornecedor_df = query_fornecedor()
    fornecedor_df.columns = ["cod_fornecedor", "desc_fornecedor", "cnpj", "iestadual"]
    #fornecedor_df.fillna(0, inplace=True)

    fornecedor_df['empresa'] = 1
    fornecedor_df = fornecedor_df.query('cod_fornecedor==16')

    _fornecedor = fornecedor_df.assign(**fornecedor_df.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict("records")

    return _fornecedor


def rotina_enviar_fornecedor():
    dados = rotina_tratando_fornecedor()
    token = login_api()

    url = 'http://177.136.201.66/api/fornecedor/'
    #url = 'http://192.168.1.121/api/fornecedor/'
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
