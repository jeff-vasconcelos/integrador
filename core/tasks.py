from __future__ import absolute_import
from celery import shared_task
#from core.calculo import soma
from core.data_db.execucoes_celery.rotina_avarias import rotina_tratando_avarias, rotina_enviar_avarias
from core.data_db.execucoes_celery.rotina_estoque_atual import rotina_tratando_estoque_atual, rotina_enviar_estoque_atual
from core.data_db.execucoes_celery.rotina_hist_estoque import rotina_tratando_hist_estoque, rotina_enviar_hist_estoque
from core.data_db.execucoes_celery.rotina_p_compras import rotina_tratando_p_compras, rotina_enviar_p_compras
from core.data_db.execucoes_celery.rotina_ultima_entrada import rotina_tratando_ultima_entrada, rotina_enviar_ultima_entrada
from core.data_db.execucoes_celery.rotina_vendas import rotina_tratando_vendas, rotina_enviar_vendas


'''
@shared_task
def realiza_soma():
    print('Feita a soma')
    soma(1,2)
'''

@shared_task
def rotina_avarias():
    print('Executando Rotina: Avarias...')
    rotina_enviar_avarias()
    print('Avarias Concluido!!!')


@shared_task
def rotina_estoque_atual():
    print('Executando Rotina: Estoque Atual...')
    rotina_enviar_estoque_atual()
    print('Estoque Atual Concluido!!!')


@shared_task
def rotina_hist_estoque():
    print('Executando Rotina: Histórico de Estoque...')
    rotina_enviar_hist_estoque()
    print('Histórico de Estoque Concluido!!!')


@shared_task
def rotina_p_compras():
    print('Executando Rotina: Preço de compras...')
    rotina_enviar_p_compras()
    print('Preço de Compras Concluido!!!')


@shared_task
def rotina_ultima_entrada():
    print('Executando Rotina: Ultima entrada...')
    rotina_enviar_ultima_entrada()
    print('Ultima Entrada Concluido!!!')


@shared_task
def rotina_vendas():
    print('Executando Rotina: Vendas...')
    rotina_enviar_vendas()
    print('Vendas Concluido!!!')
