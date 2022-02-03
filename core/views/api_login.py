import requests
from core.models.configuration import Configuration


def get_data_company():
    qs = Configuration.objects.get(id=1)
    return qs


def login_api():
    company = get_data_company()

    #url = "https://insight.ecluster.com.br/api-token-auth"
    url = "https://insight.ecluster.com.br/api/token/"
    user_data = {
        "username": "welleson",
        "password": "W180425l"
    }

    response = requests.post(url=url, json=user_data)

    if response.status_code == 200:
        response_data = response.json()
        # token_puro = response_data['token']
        token_puro = response_data['access']

        token = "Bearer "
        token += token_puro
        return token
    else:
        raise ValueError('Erro: function(login) Não foi possivel realizar login no servidor')
