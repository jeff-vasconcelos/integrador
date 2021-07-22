from core.login_api import login_api
from core.query import query_produto
import requests
import json


def rotina_tratando_produto():
    df_produtos = query_produto()
    df_produtos.columns = ["cod_fornecedor", "cod_produto", "desc_produto", "cod_ncm", "cod_auxiliar", "marca", "embalagem", "quantidade_un_cx",  "peso_liquido", "cod_fabrica", "cod_depto", "desc_departamento", "cod_sec", "desc_secao", "principio_ativo"]
    #df_produtos.fillna(0, inplace=True)

    df_produtos['empresa'] = 1

    produtos_dic = df_produtos.assign(**df_produtos.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict(
        "records")

    return produtos_dic


def rotina_enviar_produto():
    dados = rotina_tratando_produto()
    token = login_api()

    url = 'http://192.168.1.121/api/produto/'
    headers = {
        'Authorization': token,
        'content-Type': 'application/json',
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
