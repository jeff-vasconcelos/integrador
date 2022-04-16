import requests
from decouple import config


def login_api():

    user_data = {
        "username": config('COMPANY_INSIGHT_USER'),
        "password": config('COMPANY_INSIGHT_PASSWORD')
    }

    try:
        response = requests.post(url=config('URL_INSIGHT_LOGIN_API'), json=user_data)

    except requests.exceptions.RequestException as e:  # This is the correct syntax
        raise SystemExit(e)


    if response.status_code == 200:
        response_data = response.json()
        # token_puro = response_data['token']
        token_puro = response_data['access']

        token = "Bearer "
        token += token_puro
        return token
    else:
        raise ValueError('Erro: function(login) Nao foi possivel realizar login no servidor')
