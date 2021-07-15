import cx_Oracle
import pandas as pd
from django.shortcuts import render

#cx_Oracle.init_oracle_client(config_dir="/opt/oracle/instantclient_11_2/network/admin")


def conn_db():
    nnota = 1 #698098
    nfilial = 1
    con = cx_Oracle.connect(user="ESTRELA", password="star895thor", dsn="PROD")  # user, password, DNS
    cur = con.cursor()


    return cur, con


def query_ult_entrada():

    cur, con = conn_db()

    pd.set_option('display.max_rows', None)
    cur.execute('SELECT pcest.codfilial, pcest.dtultent, pcest.valorultent, pcest.qtultent QTD_ULT_ENTRADA,pcprodut.codprod , pcprodut.descricao FROM pcest, pcprodut WHERE pcest.dtultent >= TRUNC(SYSDATE) 100 AND pcprodut.codprod = pcest.codprod AND pcest.codfilial IN (1)')

    lista = []
    for resultado in cur:
        lista.append(resultado)
    res_df = pd.DataFrame(lista)
    res_df_d = res_df.dropna()
    print(res_df_d)
    print(resultado)

    cur.close()
    con.close()

    return res_df_d


def query_estoque():
    cur, con = conn_db()

    pd.set_option('display.max_rows', None)
    cur.execute('SELECT pcprodut.descricao, pcprodut.embalagem, pcest.codfilial, pcest.codprod, pcest.qtestger, pcest.qtindeniz, pcest.qtreserv, pcest.qtpendente, pcest.qtbloqueada, pcest.qtestger - (pcest.qtindeniz + pcest.qtreserv + pcest.qtpendente + pcest.qtbloqueada) AS Qtd_Disp, pcest.custoultent, pcfornec.codfornec, pcfornec.fornecedor, pctabpr.pvenda FROM pcprodut, pcest, pcfornec, pctabpr WHERE pcest.codprod = pcprodut.codprod AND pcprodut.codprod = pctabpr.codprod AND pcprodut.codfornec = pcfornec.codfornec AND pcest.codfilial in (1, 2, 3, 4, 5, 6) AND pctabpr.numregiao = 1')

    lista = []
    for resultado in cur:
        lista.append(resultado)
    res_df = pd.DataFrame(lista)
    res_df_d = res_df.dropna()
    print(res_df_d)
    print(resultado)

    cur.close()
    con.close()

    return res_df_d


def query_hist():
    cur, con = conn_db()

    pd.set_option('display.max_rows', None)
    cur.execute('SELECT pchistest.codprod, pcprodut.descricao, pcprodut.embalagem, pchistest.data, pchistest.qtestger, pchistest.codfilial FROM pchistest, pcprodut WHERE pchistest.codprod = pcprodut.codprod AND pchistest.data >= TRUNC(SYSDATE) -120 ORDER BY pchistest.codfilial, pchistest.codprod, pchistest.data')

    lista = []
    for resultado in cur:
        lista.append(resultado)
        print(resultado)
    res_df = pd.DataFrame(lista)
    res_df_d = res_df.dropna()
    print(res_df_d)
    print(resultado)

    cur.close()
    con.close()

    return res_df_d


def query_p_compras():
    cur, con = conn_db()

    pd.set_option('display.max_rows', None)
    cur.execute('SELECT pcpedido.codfilial, pcitem.codprod, pcprodut.descricao, pcitem.qtpedida - pcitem.qtentregue AS SALDO, pcitem.numped, pcpedido.dtemissao FROM pcprodut, pcitem, pcpedido WHERE pcitem.codprod = pcprodut.codprod AND pcitem.numped = pcpedido.numped AND pcpedido.dtemissao >= TRUNC(SYSDATE) - 90')

    lista = []
    for resultado in cur:
        lista.append(resultado)
    res_df = pd.DataFrame(lista)
    res_df_d = res_df.dropna()
    print(res_df_d)
    print(resultado)

    cur.close()
    con.close()

    return res_df_d


def query_p_vendas():
    cur, con = conn_db()

    pd.set_option('display.max_rows', None)
    cur.execute("SELECT pcmov.dtmov, pcprodut.codprod, pcprodut.descricao, pcmov.qt, pcmov.punit, pcmov.codfilial, pcclient.codcli, pcmov.pesoliq, pcmov.codepto, pcdepto.descricao DEPARTAMENTO, pcmov.numnota, pcmov.codusur, pcmov.codfornec, pcsecao.descricao SECAO, pcprodut.qtunitcx, pcprodut.codauxiliar, pcmov.custofin, pcmarca.marca, pcprodut.codfab, pcsuperv.nome SUPERVISOR FROM pcmov, pcdepto, pcprodut, pcsecao, pcmarca, pcclient, pcusuari, pcsuperv WHERE pcmov.dtmov >= TRUNC(SYSDATE) -120 AND pcmov.codepto = pcdepto.codepto AND pcmov.codprod = pcprodut.codprod AND pcmov.codusur = pcusuari.codusur AND pcusuari.codsupervisor = pcsuperv.codsupervisor AND pcprodut.codsec = pcsecao.codsec AND pcprodut.codmarca = pcmarca.codmarca AND pcmov.codcli = pcclient.codcli AND pcmov.codfilial IN (1, 2, 3, 4, 5, 6) AND pcmov.codoper = 'S'")

    lista = []
    for resultado in cur:
        lista.append(resultado)
    res_df = pd.DataFrame(lista)
    res_df_d = res_df.dropna()
    print(res_df_d)
    print(resultado)

    cur.close()
    con.close()

    return res_df_d
