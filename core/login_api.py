import requests


def login_api():
    usuario = 'cluster'
    senha = 'Cluster*2018'

    url = "http://177.136.201.66/api-token-auth"
    user_data = {
        "username": usuario,
        "password": senha
    }

    response = requests.post(url=url, json=user_data)

    if response.status_code == 200:
        response_data = response.json()
        token_puro = response_data['token']

        token = "Token "
        token += token_puro
        return token
