import datetime

from core.views.api_login import login_api
from core.views.query_db import queryset_oracle
from core.views.send_to_data import send_data_tasks, send_data_integration, send_data_tasks_delete
from core.views.process_query_data import (process_providers, process_products, process_sales, process_histories,
                                           process_orders, process_entries, process_stocks, process_order_duplicate)


def run_providers_task():
    token = login_api()

    select_sql = "SELECT pcfornec.codfornec, pcfornec.fornecedor, pcfornec.cgc CNPJ, pcfornec.ie INS_ESTADUAL FROM pcfornec WHERE pcfornec.revenda = 'S'"
    df_providers = queryset_oracle(select_oracle=select_sql)
    list_providers = process_providers(df_providers)
    url = "https://insight.ecluster.com.br/api/providers/"

    send_data_tasks(url, token, list_providers)


def run_products_task():
    token = login_api()

    select_sql = "SELECT pcprodut.codfornec,pcprodut.codprod,pcprodut.descricao,pcprodut.nbm ncm, pcprodut.codauxiliar ean,pcmarca.marca,pcprodut.embalagem,pcprodut.qtunitcx,pcprodut.pesoliq, pcprodut.codfab,pcprodut.codepto,pcdepto.descricao departamento,pcprodut.codsec, pcsecao.descricao secao,pcprincipativo.descricao principio_ativo FROM pcprodut, pcmarca, pcdepto, pcsecao, pcprincipativo, pcfornec WHERE pcprodut.codmarca = pcmarca.codmarca(+) AND pcprodut.codepto = pcdepto.codepto(+) AND pcprodut.codsec = pcsecao.codsec(+) AND pcprodut.codfornec = pcfornec.codfornec(+) AND pcprodut.codprincipativo = pcprincipativo.codprincipativo(+) AND pcprodut.obs2 <> 'FL' and pcprodut.dtexclusao is null"
    df_products = queryset_oracle(select_oracle=select_sql)
    list_products = process_products(df_products)

    url = "https://insight.ecluster.com.br/api/products/"
    send_data_tasks(url, token, list_products)


def run_histories_task():
    token = login_api()

    yesterday = datetime.date.today() - datetime.timedelta(days=1)

    select_sql = f"SELECT pchistest.codprod, pchistest.data, pchistest.qtestger, pchistest.codfilial, pcprodut.codfornec FROM pchistest, pcprodut WHERE pchistest.codprod = pcprodut.codprod AND pchistest.data = TO_DATE('{yesterday}','YYYY/MM/DD') ORDER BY pchistest.codfilial, pchistest.codprod, pchistest.data"
    df_histories = queryset_oracle(select_oracle=select_sql)
    list_histories = process_histories(df_histories)
    url = "https://insight.ecluster.com.br/api/stock-histories/"

    send_data_tasks(url, token, list_histories)


def run_sales_task():
    token = login_api()

    today = datetime.date.today()

    select_sql = f"SELECT pcmov.dtmov, pcprodut.codprod, pcmov.qt, pcmov.punit, pcmov.codfilial, pcclient.cliente, pcmov.numnota, pcusuari.nome RCA, pcmov.codfornec, pcmov.custofin, pcsuperv.nome SUPERVISOR FROM pcmov,pcprodut, pcclient, pcusuari, pcsuperv WHERE pcmov.dtmov = TO_DATE('{today}','YYYY/MM/DD') AND pcmov.codprod = pcprodut.codprod AND pcmov.codusur = pcusuari.codusur AND pcusuari.codsupervisor = pcsuperv.codsupervisor AND pcmov.codcli = pcclient.codcli AND pcmov.codfilial IN (1) AND pcmov.codoper = 'S'"
    df_sales = queryset_oracle(select_oracle=select_sql)
    list_sales = process_sales(df_sales)
    url = "https://insight.ecluster.com.br/api/product-sales/"

    send_data_tasks(url, token, list_sales)


def run_orders_task():
    token = login_api()

    today = datetime.date.today()
    yesterday = datetime.date.today() - datetime.timedelta(days=90)

    select_sql = f"SELECT pcpedido.codfilial, pcitem.codprod, pcitem.qtpedida - pcitem.qtentregue AS SALDO, pcitem.numped, pcpedido.dtemissao, pcprodut.codfornec FROM pcprodut, pcitem, pcpedido WHERE pcitem.codprod = pcprodut.codprod AND pcitem.numped = pcpedido.numped AND pcpedido.codfilial IN (1) AND pcpedido.dtemissao BETWEEN TO_DATE('{yesterday}','YYYY/MM/DD') AND TO_DATE('{today}','YYYY/MM/DD')"
    df_orders = queryset_oracle(select_oracle=select_sql)
    list_orders = process_orders(df_orders)
    url = "https://insight.ecluster.com.br/api/buy-orders/"

    send_data_tasks(url, token, list_orders)


def run_orders_duplicate_task():
    token = login_api()

    today = datetime.date.today()
    yesterday = datetime.date.today() - datetime.timedelta(days=90)

    select_sql = f"SELECT pcpedido.codfilial, pcitem.codprod, pcitem.qtpedida - pcitem.qtentregue AS SALDO, pcitem.numped, pcpedido.dtemissao, pcprodut.codfornec FROM pcprodut, pcitem, pcpedido WHERE pcitem.codprod = pcprodut.codprod AND pcitem.numped = pcpedido.numped AND pcpedido.codfilial IN (1) AND pcpedido.dtemissao BETWEEN TO_DATE('{yesterday}','YYYY/MM/DD') AND TO_DATE('{today}','YYYY/MM/DD')"
    df_orders_duplicate = queryset_oracle(select_oracle=select_sql)
    list_orders_duplicate, id_company = process_order_duplicate(df_orders_duplicate)
    url_duplicates = f"https://insight.ecluster.com.br/api/integration/orders-company/delete/{id_company}/"

    if len(list_orders_duplicate) != 0:
        send_data_tasks_delete(url_duplicates, token, list_orders_duplicate)


def run_entries_task():
    token = login_api()

    today = datetime.date.today()

    select_sql = f"SELECT pcest.codfilial, pcest.dtultent, pcest.valorultent, pcest.qtultent QTD_ULT_ENTRADA, pcprodut.codprod, pcprodut.codfornec FROM pcest, pcprodut WHERE pcest.dtultent = TO_DATE('{today}','YYYY/MM/DD') AND pcprodut.codprod = pcest.codprod AND pcest.codfilial IN (1)"
    df_entries = queryset_oracle(select_oracle=select_sql)
    list_entries = process_entries(df_entries)
    url = "https://insight.ecluster.com.br/api/entry-products/"

    send_data_tasks(url, token, list_entries)


def run_stocks_task():
    token = login_api()

    select_sql = f"SELECT pcest.codfilial, pcest.codprod, pcest.qtestger, pcest.qtindeniz, pcest.qtreserv, pcest.qtpendente, pcest.qtbloqueada, pcest.qtestger - ((pcest.qtindeniz + pcest.qtreserv + pcest.qtpendente + pcest.qtbloqueada) - pcest.qtindeniz) AS Qtd_Disp, pcest.custoultent, pcfornec.codfornec, pctabpr.pvenda FROM pcprodut, pcest, pcfornec, pctabpr WHERE pcest.codprod = pcprodut.codprod AND pcprodut.codprod = pctabpr.codprod AND pcprodut.codfornec = pcfornec.codfornec AND pcest.codfilial in (1) AND pctabpr.numregiao = 1 AND pcprodut.obs2 <> 'FL' AND pcprodut.dtexclusao is null"
    df_stocks = queryset_oracle(select_oracle=select_sql)
    list_stocks = process_stocks(df_stocks)
    url = "https://insight.ecluster.com.br/api/stock-current/"

    send_data_tasks(url, token, list_stocks)
