from core.views.get_data import *
from core.views.api_login import login_api
from core.views.query_db import *
from core.views.process_data import *
from core.views.send_data import *


def run_fornecedores(integration=''):
    select_sql = "SELECT pcfornec.codfornec, pcfornec.fornecedor, pcfornec.cgc CNPJ, pcfornec.ie INS_ESTADUAL FROM pcfornec WHERE pcfornec.revenda = 'S'"

    token = login_api()

    df_fornecedores = queryset_oracle(select_oracle=select_sql)

    if integration:
        url = "https://insight.ecluster.com.br/api/integration/providers/"
        lista_fornecedores = process_fornecedores(df_fornecedores)
        send_data_integration(url, token, lista_fornecedores)

    else:
        url = "https://insight.ecluster.com.br/api/providers/"
        lista_fornecedores = process_fornecedores(df_fornecedores)
        send_data_tasks(url, token, lista_fornecedores)


def run_produtos(integration=''):
    select_sql = "SELECT pcprodut.codfornec,pcprodut.codprod,pcprodut.descricao,pcprodut.nbm ncm, pcprodut.codauxiliar ean,pcmarca.marca,pcprodut.embalagem,pcprodut.qtunitcx,pcprodut.pesoliq, pcprodut.codfab,pcprodut.codepto,pcdepto.descricao departamento,pcprodut.codsec, pcsecao.descricao secao,pcprincipativo.descricao principio_ativo FROM pcprodut, pcmarca, pcdepto, pcsecao, pcprincipativo, pcfornec WHERE pcprodut.codmarca = pcmarca.codmarca(+) AND pcprodut.codepto = pcdepto.codepto(+) AND pcprodut.codsec = pcsecao.codsec(+) AND pcprodut.codfornec = pcfornec.codfornec(+) AND pcprodut.codprincipativo = pcprincipativo.codprincipativo(+) AND pcprodut.obs2 <> 'FL' and pcprodut.dtexclusao is null"

    token = login_api()

    df_produtos = queryset_oracle(select_oracle=select_sql)
    lista_produtos = process_produtos(df_produtos)

    if integration:
        url = "https://insight.ecluster.com.br/api/integration/products/"
        send_data_integration(url, token, lista_produtos)

    else:
        url = "https://insight.ecluster.com.br/api/products/"
        send_data_tasks(url, token, lista_produtos)


def run_historico(dt_inicio, dt_fim, integration=''):
    select_sql = f"SELECT pchistest.codprod, pchistest.data, pchistest.qtestger, pchistest.codfilial, pcprodut.codfornec FROM pchistest, pcprodut WHERE pchistest.codprod = pcprodut.codprod AND pchistest.data BETWEEN TO_DATE('{dt_inicio}','YYYY/MM/DD') AND TO_DATE('{dt_fim}','YYYY/MM/DD') ORDER BY pchistest.codfilial, pchistest.codprod, pchistest.data"

    token = login_api()

    df_historico = queryset_oracle(select_oracle=select_sql)

    if integration:
        url = "https://insight.ecluster.com.br/api/integration/stock-histories/"
        lista_historico = process_historico(df_historico, True)
        send_data_integration(url, token, lista_historico)

    else:
        url = "https://insight.ecluster.com.br/api/stock-histories/"
        lista_historico = process_historico(df_historico, False)
        send_data_tasks(url, token, lista_historico)


def run_vendas(dt_inicio, dt_fim, integration=''):
    select_sql = f"SELECT pcmov.dtmov, pcprodut.codprod, pcmov.qt, pcmov.punit, pcmov.codfilial, pcclient.cliente, pcmov.numnota, pcusuari.nome RCA, pcmov.codfornec, pcmov.custofin, pcsuperv.nome SUPERVISOR FROM pcmov,pcprodut, pcclient, pcusuari, pcsuperv WHERE pcmov.dtmov BETWEEN TO_DATE('{dt_inicio}','YYYY/MM/DD') AND TO_DATE('{dt_fim}','YYYY/MM/DD') AND pcmov.codprod = pcprodut.codprod AND pcmov.codusur = pcusuari.codusur AND pcusuari.codsupervisor = pcsuperv.codsupervisor AND pcmov.codcli = pcclient.codcli AND pcmov.codfilial IN (1) AND pcmov.codoper = 'S'"

    token = login_api()

    df_vendas = queryset_oracle(select_oracle=select_sql)

    if integration:
        url = "https://insight.ecluster.com.br/api/integration/product-sales/"
        lista_vendas = process_vendas(df_vendas, True)
        send_data_integration(url, token, lista_vendas)

    else:
        url = "https://insight.ecluster.com.br/api/product-sales/"
        lista_vendas = process_vendas(df_vendas, False)
        send_data_tasks(url, token, lista_vendas)


def run_pedidos(dt_inicio, dt_fim, integration=''):
    select_sql = f"SELECT pcpedido.codfilial, pcitem.codprod, pcitem.qtpedida - pcitem.qtentregue AS SALDO, pcitem.numped, pcpedido.dtemissao, pcprodut.codfornec FROM pcprodut, pcitem, pcpedido WHERE pcitem.codprod = pcprodut.codprod AND pcitem.numped = pcpedido.numped AND pcpedido.codfilial IN (1) AND pcpedido.dtemissao BETWEEN TO_DATE('{dt_inicio}','YYYY/MM/DD') AND TO_DATE('{dt_fim}','YYYY/MM/DD')"

    token = login_api()

    df_pedidos = queryset_oracle(select_oracle=select_sql)

    if integration:
        url = "https://insight.ecluster.com.br/api/integration/buy-orders/"
        lista_pedidos = process_pedidos(df_pedidos, True)
        send_data_integration(url, token, lista_pedidos)

    else:
        url = "https://insight.ecluster.com.br/api/buy-orders/"
        lista_pedidos = process_pedidos(df_pedidos, False)
        send_data_tasks(url, token, lista_pedidos)

        # REMOVENDO PEDIDOS APAGADOS DO ERP
        list_orders_duplicate, id_company = process_order_duplicate(df_pedidos)
        url_duplicates = f"https://insight.ecluster.com.br/api/integration/orders-company/delete/{id_company}/"
        send_data_tasks(url_duplicates, token, list_orders_duplicate)


def run_entradas(dt_inicio, dt_fim, integration=''):
    select_sql = f"SELECT pcest.codfilial, pcest.dtultent, pcest.valorultent, pcest.qtultent QTD_ULT_ENTRADA, pcprodut.codprod, pcprodut.codfornec FROM pcest, pcprodut WHERE pcest.dtultent BETWEEN TO_DATE('{dt_inicio}','YYYY/MM/DD') AND TO_DATE('{dt_fim}','YYYY/MM/DD') AND pcprodut.codprod = pcest.codprod AND pcest.codfilial IN (1)"

    token = login_api()

    df_entradas = queryset_oracle(select_oracle=select_sql)

    if integration:
        url = "https://insight.ecluster.com.br/api/integration/entry-products/"
        lista_entradas = process_entradas(df_entradas, True)
        send_data_integration(url, token, lista_entradas)

    else:
        url = "https://insight.ecluster.com.br/api/entry-products/"
        lista_entradas = process_entradas(df_entradas, False)
        send_data_tasks(url, token, lista_entradas)


def run_estoque(integration=''):
    select_sql = f"SELECT pcest.codfilial, pcest.codprod, pcest.qtestger, pcest.qtindeniz, pcest.qtreserv, pcest.qtpendente, pcest.qtbloqueada, pcest.qtestger - ((pcest.qtindeniz + pcest.qtreserv + pcest.qtpendente + pcest.qtbloqueada) - pcest.qtindeniz) AS Qtd_Disp, pcest.custoultent, pcfornec.codfornec, pctabpr.pvenda FROM pcprodut, pcest, pcfornec, pctabpr WHERE pcest.codprod = pcprodut.codprod AND pcprodut.codprod = pctabpr.codprod AND pcprodut.codfornec = pcfornec.codfornec AND pcest.codfilial in (1) AND pctabpr.numregiao = 1 AND pcprodut.obs2 <> 'FL' AND pcprodut.dtexclusao is null"

    token = login_api()

    df_estoque = queryset_oracle(select_oracle=select_sql)

    if integration:
        url = "https://insight.ecluster.com.br/api/integration/stock-current/"
        lista_estoque = process_estoque(df_estoque, True)

        send_data_integration(url, token, lista_estoque)

    else:
        url = "https://insight.ecluster.com.br/api/stock-current/"
        lista_estoque = process_estoque(df_estoque, False)
        send_data_tasks(url, token, lista_estoque)
