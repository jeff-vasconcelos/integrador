from __future__ import absolute_import, unicode_literals
from celery import shared_task

import datetime
from core.models.providers import Provider
from core.views.get_data import register_log
from core.views.tasks_integration import (run_providers_task, run_products_task, run_histories_task, run_sales_task,
                                          run_orders_task, run_entries_task, run_stocks_task, run_orders_duplicate_task)

from core.views.api_login import get_data_company
from core.write_query_data.provider import writer_provider
from core.write_query_data.product import writer_product
from core.write_query_data.history import writer_history
from core.write_query_data.sale import writer_sale
from core.write_query_data.entry import writer_entry
from core.write_query_data.orders import writer_order
from core.write_query_data.stock import writer_stock
from core.views.query_db import queryset_oracle
from core.views.process_query_data import (process_providers, process_products, process_sales, process_histories,
                                           process_orders, process_entries, process_stocks, process_order_duplicate)


@shared_task
def task_provider():
    try:

        # executando consulta no oracle
        select_sql = "SELECT pcfornec.codfornec, pcfornec.fornecedor, pcfornec.cgc CNPJ, pcfornec.ie INS_ESTADUAL FROM pcfornec WHERE pcfornec.revenda = 'S'"
        df_providers = queryset_oracle(select_oracle=select_sql)

        # criando dataframe de fornecedores passando task=True para retornar um dataframe
        dataframe_providers = process_providers(df_providers=df_providers, task=True)

        # gravando dados no banco local para otimização de envios
        writer_provider(dataframe_providers)

        # executando tarefa de envio de dados para o insight web
        run_providers_task()

    except ValueError as err:
        error = f"(Task) Fornecedor - {str(err)}"
        register_log(error)


@shared_task
def task_product():
    try:

        # executando consulta no oracle
        select_sql = "SELECT pcprodut.codfornec,pcprodut.codprod,pcprodut.descricao,pcprodut.nbm ncm, pcprodut.codauxiliar ean,pcmarca.marca,pcprodut.embalagem,pcprodut.qtunitcx,pcprodut.pesoliq, pcprodut.codfab,pcprodut.codepto,pcdepto.descricao departamento,pcprodut.codsec, pcsecao.descricao secao,pcprincipativo.descricao principio_ativo FROM pcprodut, pcmarca, pcdepto, pcsecao, pcprincipativo, pcfornec WHERE pcprodut.codmarca = pcmarca.codmarca(+) AND pcprodut.codepto = pcdepto.codepto(+) AND pcprodut.codsec = pcsecao.codsec(+) AND pcprodut.codfornec = pcfornec.codfornec(+) AND pcprodut.codprincipativo = pcprincipativo.codprincipativo(+) AND pcprodut.obs2 <> 'FL' and pcprodut.dtexclusao is null"
        df_products = queryset_oracle(select_oracle=select_sql)

        # criando dataframe de produtos passando task=True para retornar um dataframe
        dataframe_products = process_products(df_products=df_products, task=True)

        # gravando dados no banco local para otimização de envios
        writer_product(dataframe_products)

        # executando tarefa de envio de dados para o insight web
        run_products_task()


    except ValueError as err:
        error = f"(Task) Produto - {str(err)}"
        register_log(error)


@shared_task
def task_history():
    try:
        today = datetime.date.today()
        yesterday = datetime.date.today() - datetime.timedelta(days=1)

        # executando consulta no oracle
        select_sql = f"SELECT pchistest.codprod, pchistest.data, pchistest.qtestger, pchistest.codfilial, pcprodut.codfornec FROM pchistest, pcprodut WHERE pchistest.codprod = pcprodut.codprod AND pchistest.data BETWEEN TO_DATE('{yesterday}','YYYY/MM/DD') AND TO_DATE('{today}','YYYY/MM/DD') ORDER BY pchistest.codfilial, pchistest.codprod, pchistest.data"
        df_histories = queryset_oracle(select_oracle=select_sql)

        # criando dataframe de historico passando task=True para retornar um dataframe
        dataframe_histories = process_histories(df_histories, task=True)

        # gravando dados no banco local para otimização de envios
        writer_history(dataframe_histories)

        # executando tarefa de envio de dados para o insight web
        run_histories_task()

    except ValueError as err:
        error = f"(Task) Histórico - {str(err)}"
        register_log(error)


@shared_task
def task_sale():
    try:
        today = datetime.date.today()
        yesterday = datetime.date.today() - datetime.timedelta(days=1)

        # executando consulta no oracle
        select_sql = f"SELECT pcmov.dtmov, pcprodut.codprod, pcmov.qt, pcmov.punit, pcmov.codfilial, pcclient.cliente, pcmov.numnota, pcusuari.nome RCA, pcmov.codfornec, pcmov.custofin, pcsuperv.nome SUPERVISOR FROM pcmov,pcprodut, pcclient, pcusuari, pcsuperv WHERE pcmov.dtmov BETWEEN TO_DATE('{yesterday}','YYYY/MM/DD') AND TO_DATE('{today}','YYYY/MM/DD') AND pcmov.codprod = pcprodut.codprod AND pcmov.codusur = pcusuari.codusur AND pcusuari.codsupervisor = pcsuperv.codsupervisor AND pcmov.codcli = pcclient.codcli AND pcmov.codfilial IN (1) AND pcmov.codoper = 'S'"
        df_sales = queryset_oracle(select_oracle=select_sql)

        # criando dataframe de vendas passando task=True para retornar um dataframe
        dataframe_sales = process_sales(df_sales, task=True)

        # gravando dados no banco local para otimização de envios
        writer_sale(dataframe_sales)

        # executando tarefa de envio de dados para o insight web
        run_sales_task()

    except ValueError as err:
        error = f"(Task) Vendas - {str(err)}"
        register_log(error)


@shared_task
def task_order():
    try:
        today = datetime.date.today()
        yesterday = datetime.date.today() - datetime.timedelta(days=1)

        # executando consulta no oracle
        select_sql = f"SELECT pcpedido.codfilial, pcitem.codprod, pcitem.qtpedida - pcitem.qtentregue AS SALDO, pcitem.numped, pcpedido.dtemissao, pcprodut.codfornec FROM pcprodut, pcitem, pcpedido WHERE pcitem.codprod = pcprodut.codprod AND pcitem.numped = pcpedido.numped AND pcpedido.codfilial IN (1) AND pcpedido.dtemissao BETWEEN TO_DATE('{yesterday}','YYYY/MM/DD') AND TO_DATE('{today}','YYYY/MM/DD')"
        df_orders = queryset_oracle(select_oracle=select_sql)

        # criando dataframe de pedidos passando task=True para retornar um dataframe
        dataframe_orders = process_orders(df_orders, task=True)

        # gravando dados no banco local para otimização de envios
        writer_order(dataframe_orders)

        # executando tarefa de envio de dados para o insight web
        run_orders_task()

    except ValueError as err:
        error = f"(Task) Pedidos - {str(err)}"
        register_log(error)


@shared_task
def task_orders_duplicate():
    try:

        run_orders_duplicate_task()

    except ValueError as err:
        error = f"(Task) Pedidos - {str(err)}"
        register_log(error)


@shared_task
def task_entry():
    try:
        today = datetime.date.today()
        yesterday = datetime.date.today() - datetime.timedelta(days=1)

        # executando consulta no oracle
        select_sql = f"SELECT pcest.codfilial, pcest.dtultent, pcest.valorultent, pcest.qtultent QTD_ULT_ENTRADA, pcprodut.codprod, pcprodut.codfornec FROM pcest, pcprodut WHERE pcest.dtultent BETWEEN TO_DATE('{yesterday}','YYYY/MM/DD') AND TO_DATE('{today}','YYYY/MM/DD') AND pcprodut.codprod = pcest.codprod AND pcest.codfilial IN (1)"
        df_entries = queryset_oracle(select_oracle=select_sql)

        # criando dataframe de entradas passando task=True para retornar um dataframe
        dataframe_entries = process_entries(df_entries, task=True)

        # gravando dados no banco local para otimização de envios
        writer_entry(dataframe_entries)

        # executando tarefa de envio de dados para o insight web
        run_entries_task()

    except ValueError as err:
        error = f"(Task) Entradas - {str(err)}"
        register_log(error)


@shared_task
def task_stock():
    try:
        # executando consulta no oracle
        select_sql = f"SELECT pcest.codfilial, pcest.codprod, pcest.qtestger, pcest.qtindeniz, pcest.qtreserv, pcest.qtpendente, pcest.qtbloqueada, pcest.qtestger - ((pcest.qtindeniz + pcest.qtreserv + pcest.qtpendente + pcest.qtbloqueada) - pcest.qtindeniz) AS Qtd_Disp, pcest.custoultent, pcfornec.codfornec, pctabpr.pvenda FROM pcprodut, pcest, pcfornec, pctabpr WHERE pcest.codprod = pcprodut.codprod AND pcprodut.codprod = pctabpr.codprod AND pcprodut.codfornec = pcfornec.codfornec AND pcest.codfilial in (1) AND pctabpr.numregiao = 1 AND pcprodut.obs2 <> 'FL' AND pcprodut.dtexclusao is null"
        df_stocks = queryset_oracle(select_oracle=select_sql)

        # criando dataframe de entradas passando task=True para retornar um dataframe
        dataframe_stocks = process_stocks(df_stocks, task=True)

        # gravando dados no banco local para otimização de envios
        writer_stock(dataframe_stocks)

        # executando tarefa de envio de dados para o insight web
        run_stocks_task()

    except ValueError as err:
        error = f"(Task) Estoque - {str(err)}"
        register_log(error)
