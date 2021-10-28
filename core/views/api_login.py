import requests
from core.models import Configuracao


def get_data_business():
    qs = Configuracao.objects.get(id=1)
    return qs


def login_api():
    business = get_data_business()

    url = "https://insight.ecluster.com.br/api-token-auth"
    user_data = {
        "username": business.username,
        "password": business.password
    }

    response = requests.post(url=url, json=user_data)

    if response.status_code == 200:
        response_data = response.json()
        token_puro = response_data['token']

        token = "Token "
        token += token_puro
        return token
