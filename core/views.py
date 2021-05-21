from django.shortcuts import render
from core.models import Parametros
import requests


def home(request, template_name='base.html'):
    return render(request, template_name)


def login_api():
    parametros = Parametros.objects.all()
    user = parametros.username
    passw = parametros.password

    url = "http://127.0.0.1:8000/api-token-auth"
    user_data = {
        "username": user,
        "password": passw
    }

    response = requests.post(url=url, json=user_data)

    if response.status_code == 200:
        response_data = response.json()
        token_puro = response_data['token']

        token = "Token "
        token += token_puro
        return token
