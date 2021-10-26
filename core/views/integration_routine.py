from core.views.get_data import *
from core.views.login_api import login_api
from core.views.query_db import *
from core.views.process_data import *
from core.views.send_data import *


def run_fornecedor(integration=''):
    select_sql = "SELECT pcfornec.codfornec, pcfornec.fornecedor, pcfornec.cgc CNPJ, pcfornec.ie INS_ESTADUAL " \
                 "FROM pcfornec WHERE pcfornec.revenda = 'S'"

    token = login_api()

    df_fornecedores = queryset_oracle(select_oracle=select_sql)

    if integration:
        url = "https://insight.ecluster.com.br/api/integration/fornecedor/"
        lista_fornecedores = process_fornecedores(df_fornecedores)
        send_data_integration(url, token, lista_fornecedores)

    else:
        url = "https://insight.ecluster.com.br/api/fornecedor/"
        lista_fornecedores = process_fornecedores(df_fornecedores)
        send_data_tasks(url, token, lista_fornecedores)


def run_produto(integration=''):
    select_sql = "SELECT pcprodut.codfornec,pcprodut.codprod,pcprodut.descricao,pcprodut.nbm ncm," \
                 "pcprodut.codauxiliar ean,pcmarca.marca,pcprodut.embalagem,pcprodut.qtunitcx,pcprodut.pesoliq," \
                 "pcprodut.codfab,pcprodut.codepto,pcdepto.descricao departamento,pcprodut.codsec," \
                 "pcsecao.descricao secao,pcprincipativo.descricao principio_ativo " \
                 "FROM pcprodut, pcmarca, pcdepto, pcsecao, pcprincipativo, pcfornec " \
                 "WHERE pcprodut.codmarca = pcmarca.codmarca(+) " \
                 "AND pcprodut.codepto = pcdepto.codepto(+) " \
                 "AND pcprodut.codsec = pcsecao.codsec(+) " \
                 "AND pcprodut.codfornec = pcfornec.codfornec(+) " \
                 "AND pcprodut.codprincipativo = pcprincipativo.codprincipativo(+) " \
                 "AND pcprodut.obs2 <> 'FL' and pcprodut.dtexclusao is null"

    token = login_api()

    df_produtos = queryset_oracle(select_oracle=select_sql)
    lista_produtos = process_produtos(df_produtos)

    if integration:
        url = "https://insight.ecluster.com.br/api/integration/produto/"
        send_data_integration(url, token, lista_produtos)

    else:
        url = "https://insight.ecluster.com.br/api/produto/"
        send_data_tasks(url, token, lista_produtos)


def run_historico(dt_inicio, dt_fim, integration=''):
    select_sql = f"SELECT pchistest.codprod, pchistest.data, pchistest.qtestger, pchistest.codfilial, " \
                 f"pcprodut.codfornec " \
                 f"FROM pchistest, pcprodut " \
                 f"WHERE pchistest.codprod = pcprodut.codprod AND pchistest.data " \
                 f"BETWEEN TO_DATE('{dt_inicio}','DD/MM/YYYY') AND TO_DATE('{dt_fim}','DD/MM/YYYY') " \
                 f"ORDER BY pchistest.codfilial, pchistest.codprod, pchistest.data"

    token = login_api()

    df_historico = queryset_oracle(select_oracle=select_sql)

    if integration:
        url = "https://insight.ecluster.com.br/api/integration/historico/"
        lista_historico = process_historico(df_historico, True)
        send_data_integration(url, token, lista_historico)

    else:
        url = "https://insight.ecluster.com.br/api/historico/"
        lista_historico = process_historico(df_historico, False)
        send_data_tasks(url, token, lista_historico)


def run_vendas(dt_inicio, dt_fim, integration=''):
    select_sql = f"SELECT pcmov.dtmov, pcprodut.codprod, pcmov.qt, pcmov.punit, pcmov.codfilial, pcclient.cliente," \
                 f" pcmov.numnota, pcusuari.nome RCA, pcmov.codfornec, pcmov.custofin, pcsuperv.nome SUPERVISOR " \
                 f"FROM pcmov,pcprodut, pcclient, pcusuari, pcsuperv " \
                 f"WHERE pcmov.dtmov BETWEEN TO_DATE('{dt_inicio}','DD/MM/YYYY') AND TO_DATE('{dt_fim}','DD/MM/YYYY') " \
                 f"AND pcmov.codprod = pcprodut.codprod AND pcmov.codusur = pcusuari.codusur " \
                 f"AND pcusuari.codsupervisor = pcsuperv.codsupervisor AND pcmov.codcli = pcclient.codcli " \
                 f"AND pcmov.codfilial IN (1) AND pcmov.codoper = 'S'"

    token = login_api()

    df_vendas = queryset_oracle(select_oracle=select_sql)

    if integration:
        url = "https://insight.ecluster.com.br/api/integration/vendas/"
        lista_vendas = process_vendas(df_vendas, True)
        send_data_integration(url, token, lista_vendas)

    else:
        url = "https://insight.ecluster.com.br/api/vendas/"
        lista_vendas = process_vendas(df_vendas, False)
        send_data_tasks(url, token, lista_vendas)


def run_pedidos(dt_inicio, dt_fim, integration=''):
    select_sql = f"SELECT pcpedido.codfilial, pcitem.codprod, pcitem.qtpedida - pcitem.qtentregue " \
                 f"AS SALDO, pcitem.numped, pcpedido.dtemissao, pcprodut.codfornec FROM pcprodut, pcitem, pcpedido " \
                 f"WHERE pcitem.codprod = pcprodut.codprod AND pcitem.numped = pcpedido.numped " \
                 f"AND pcpedido.codfilial IN (1) AND pcpedido.dtemissao " \
                 f"BETWEEN TO_DATE('{dt_inicio}','DD/MM/YYYY') AND TO_DATE('{dt_fim}','DD/MM/YYYY')"

    token = login_api()

    df_pedidos = queryset_oracle(select_oracle=select_sql)

    if integration:
        url = "https://insight.ecluster.com.br/api/integration/pedidos/"
        lista_pedidos = process_pedidos(df_pedidos, True)
        send_data_integration(url, token, lista_pedidos)

    else:
        url = "https://insight.ecluster.com.br/api/pedidos/"
        lista_pedidos = process_pedidos(df_pedidos, False)
        send_data_tasks(url, token, lista_pedidos)


def run_entradas(dt_inicio, dt_fim, integration=''):
    select_sql = f"SELECT pcest.codfilial, pcest.dtultent, pcest.valorultent, pcest.qtultent QTD_ULT_ENTRADA, " \
                 f"pcprodut.codprod, pcprodut.codfornec FROM pcest, pcprodut WHERE pcest.dtultent " \
                 f"BETWEEN TO_DATE('{dt_inicio}','DD/MM/YYYY') AND TO_DATE('{dt_fim}','DD/MM/YYYY') " \
                 f"AND pcprodut.codprod = pcest.codprod AND pcest.codfilial IN (1)"

    token = login_api()

    df_entradas = queryset_oracle(select_oracle=select_sql)

    if integration:
        url = "https://insight.ecluster.com.br/api/integration/entradas/"
        lista_entradas = process_entradas(df_entradas, True)
        send_data_integration(url, token, lista_entradas)

    else:
        url = "https://insight.ecluster.com.br/api/entradas/"
        lista_entradas = process_entradas(df_entradas, False)
        send_data_tasks(url, token, lista_entradas)


def run_estoque(integration=''):
    select_sql = f"SELECT pcest.codfilial, pcest.codprod, pcest.qtestger, pcest.qtindeniz, pcest.qtreserv, " \
                 f"pcest.qtpendente, pcest.qtbloqueada, pcest.qtestger - ((pcest.qtindeniz + pcest.qtreserv + " \
                 f"pcest.qtpendente + pcest.qtbloqueada) - pcest.qtindeniz) " \
                 f"AS Qtd_Disp, pcest.custoultent, pcfornec.codfornec, pctabpr.pvenda " \
                 f"FROM pcprodut, pcest, pcfornec, pctabpr WHERE pcest.codprod = pcprodut.codprod " \
                 f"AND pcprodut.codprod = pctabpr.codprod AND pcprodut.codfornec = pcfornec.codfornec " \
                 f"AND pcest.codfilial in (1) AND pctabpr.numregiao = 1 AND pcprodut.obs2 <> 'FL' " \
                 f"AND pcprodut.dtexclusao is null"

    token = login_api()

    df_estoque = queryset_oracle(select_oracle=select_sql)

    if integration:
        url = "https://insight.ecluster.com.br/api/integration/entradas/"
        lista_estoque = process_estoque(df_estoque, True)
        send_data_integration(url, token, lista_estoque)

    else:
        url = "https://insight.ecluster.com.br/api/entradas/"
        lista_estoque = process_estoque(df_estoque, False)
        send_data_tasks(url, token, lista_estoque)
