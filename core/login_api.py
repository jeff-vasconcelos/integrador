import requests


def login_api():
    usuario = 'leandroauzier'
    senha = 'a1a3A2A4'

    url = "http://127.0.0.1:8000/api-token-auth"
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
