from django.shortcuts import render
from core.models import Parametros
from core.data_db.execucoes_integracao.avarias import tratando_avarias, enviar_avarias
from core.data_db.execucoes_integracao.estoque_atual import tratando_estoque_atual, enviar_estoque_atual
from core.data_db.execucoes_integracao.hist_estoque import tratando_hist_estoque, enviar_hist_estoque
from core.data_db.execucoes_integracao.p_compras import tratando_p_compras, enviar_p_compras
from core.data_db.execucoes_integracao.ultima_entrada import tratando_ultima_entrada, enviar_ultima_entrada
from core.data_db.execucoes_integracao.vendas import tratando_vendas, enviar_vendas

from core.data_db.execucoes_celery.rotina_avarias import rotina_tratando_avarias, rotina_enviar_avarias
from core.data_db.execucoes_celery.rotina_estoque_atual import rotina_tratando_estoque_atual, rotina_enviar_estoque_atual
from core.data_db.execucoes_celery.rotina_hist_estoque import rotina_tratando_hist_estoque, rotina_enviar_hist_estoque
from core.data_db.execucoes_celery.rotina_p_compras import rotina_tratando_p_compras, rotina_enviar_p_compras
from core.data_db.execucoes_celery.rotina_ultima_entrada import rotina_tratando_ultima_entrada, rotina_enviar_ultima_entrada
from core.data_db.execucoes_celery.rotina_vendas import rotina_tratando_vendas, rotina_enviar_vendas


from core.query_oracle.query_integracao.avarias_db import avarias_db
import requests


def home(request, template_name='base.html'):
    #nada
    return render(request, template_name)


def avarias(request, template_name='base.html'):
    avaria = enviar_avarias()
    print(avaria)
    return render(request, template_name)


def estoque_atual(request, template_name='base.html'):
    estoqueAtual = enviar_estoque_atual()
    print(estoqueAtual)
    return render(request, template_name)



def hist_estoque(request, template_name='base.hmtl'):
    histEstoque = enviar_hist_estoque()
    print(histEstoque)
    return render(request, template_name)


def p_compras(request, template_name='base.html'):
    pCompras = enviar_p_compras()
    print(pCompras)
    return render(request, template_name)


def ultima_entrada(request, template_name='base.html'):
    ultimaEntrada = enviar_ultima_entrada()
    print(ultimaEntrada)
    return render(request, template_name)


def vendas(resquest, template_name='base.html'):
    venda = enviar_vendas()
    print(venda)
    return render(request, template_name='base.html')


def rotina_avarias(request, template_name='base.html'):
    avaria = rotina_enviar_avarias()
    print(avaria)
    return render(request, template_name)


def rotina_estoque_atual(request, template_name='base.html'):
    estoqueAtual = rotina_enviar_estoque_atual()
    print(estoqueAtual)
    return render(request, template_name)



def rotina_hist_estoque(request, template_name='base.hmtl'):
    histEstoque = rotina_enviar_hist_estoque()
    print(histEstoque)
    return render(request, template_name)


def rotina_p_compras(request, template_name='base.html'):
    pCompras = rotina_enviar_p_compras()
    print(pCompras)
    return render(request, template_name)


def rotina_ultima_entrada(request, template_name='base.html'):
    ultimaEntrada = rotina_enviar_ultima_entrada()
    print(ultimaEntrada)
    return render(request, template_name)

def rotina_vendas(resquest, template_name='base.html'):
    venda = rotina_enviar_vendas()
    print(venda)
    return render(request, template_name='base.html')
