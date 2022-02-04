import requests
from core.models.configuration import Configuration


def get_data_company():
    qs = Configuration.objects.get(id=1)
    return qs


def login_api():
    company = get_data_company()

    url = "https://insight.ecluster.com.br/api/token/"
    # url = "http://127.0.0.1:7000/api/token/"

    user_data = {
        "username": company.username,
        "password": company.password
    }


    try:
        response = requests.post(url=url, json=user_data)

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
