from __future__ import absolute_import, unicode_literals
from celery import shared_task
from core.data_db.execucoes_celery.rotina_estoque_atual import rotina_enviar_estoque_atual
from core.data_db.execucoes_celery.rotina_fornecedor import rotina_enviar_fornecedor
from core.data_db.execucoes_celery.rotina_hist_estoque import rotina_enviar_hist_estoque
from core.data_db.execucoes_celery.rotina_p_compras import rotina_enviar_p_compras
from core.data_db.execucoes_celery.rotina_produto import rotina_enviar_produto
from core.data_db.execucoes_celery.rotina_ultima_entrada import rotina_enviar_ultima_entrada
from core.data_db.execucoes_celery.rotina_vendas import rotina_enviar_vendas


@shared_task
def rotina_estoque_atual():
    print('Executando Rotina: Estoque Atual...')
    rotina_enviar_estoque_atual()
    print('Estoque Atual Concluido!!!')


@shared_task
def rotina_fornecedor():
    print('Executando Rotina: Fornecedor...')
    rotina_enviar_fornecedor()
    print('Fornecedor Concluido!!!')


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
def rotina_produtos():
    print('Executando Rotina: Produtos...')
    rotina_enviar_produto()
    print('Produtos Concluido!!!')


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
