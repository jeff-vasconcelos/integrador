from django.shortcuts import render
from core.models import Parametros
from core.data_db.avarias import tratando_avarias, enviar_avarias
from core.data_db.estoque_atual import tratando_estoque_atual, enviar_estoque_atual
from core.data_db.hist_estoque import tratando_hist_estoque, enviar_hist_estoque
from core.data_db.p_compras import tratando_p_compras, enviar_p_compras
from core.data_db.ultima_entrada import tratando_ultima_entrada, enviar_ultima_entrada
from core.data_db.vendas import tratando_vendas, enviar_vendas
from core.query_oracle.avarias_db import avarias_db
import requests


def home(request, template_name='base.html'):
    #teste = enviar_avarias()
    #teste2 = enviar_estoque_atual()
    #teste3 = enviar_hist_estoque()
    #teste4 = enviar_p_compras()
    #teste5 = enviar_ultima_entrada()
    teste6 = enviar_vendas()
    #print(teste)
    #print(teste2)
    #print(teste3)
    #print(teste4)
    #print(teste5)
    print(teste6)
    return render(request, template_name)


