import cx_Oracle
import pandas as pd


def conn_db():
    con = cx_Oracle.connect(user="ESTRELA", password="star895thor", dsn="PROD")  # user, password, DNS
    cur = con.cursor()

    return cur, con


def query_ult_entrada():

    cur, con = conn_db()

    cur.execute('SELECT pcest.codfilial, pcest.dtultent, pcest.valorultent, pcest.qtultent QTD_ULT_ENTRADA, pcprodut.codprod, pcprodut.codfornec FROM pcest, pcprodut WHERE pcest.dtultent >= TRUNC(SYSDATE) -120 AND pcprodut.codprod = pcest.codprod AND pcest.codfilial IN (1)')

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

    cur.execute('SELECT pcest.codfilial, pcest.codprod, pcest.qtestger, pcest.qtindeniz, pcest.qtreserv, pcest.qtpendente, pcest.qtbloqueada, pcest.qtestger - (pcest.qtindeniz + pcest.qtreserv + pcest.qtpendente + pcest.qtbloqueada) AS Qtd_Disp, pcest.custoultent, pcfornec.codfornec, pctabpr.pvenda FROM pcprodut, pcest, pcfornec, pctabpr WHERE pcest.codprod = pcprodut.codprod AND pcprodut.codprod = pctabpr.codprod AND pcprodut.codfornec = pcfornec.codfornec AND pcest.codfilial in (1) AND pctabpr.numregiao = 1')

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

    cur.execute('SELECT pchistest.codprod, pchistest.data, pchistest.qtestger, pchistest.codfilial, pcprodut.codfornec FROM pchistest, pcprodut WHERE pchistest.codprod = pcprodut.codprod AND pchistest.data >= TRUNC(SYSDATE) -120 ORDER BY pchistest.codfilial, pchistest.codprod, pchistest.data')

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

    cur.execute('SELECT pcpedido.codfilial, pcitem.codprod, pcitem.qtpedida - pcitem.qtentregue AS SALDO, pcitem.numped, pcpedido.dtemissao, pcprodut.codfornec FROM pcprodut, pcitem, pcpedido WHERE pcitem.codprod = pcprodut.codprod AND pcitem.numped = pcpedido.numped AND pcpedido.codfilial IN (1) AND pcpedido.dtemissao >= TRUNC(SYSDATE) - 120')

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

    cur.execute("select pcmov.dtmov, pcprodut.codprod, pcmov.qt, pcmov.punit, pcmov.codfilial, pcclient.cliente, pcmov.numnota, pcusuari.nome RCA, pcmov.codfornec, pcmov.custofin, pcsuperv.nome SUPERVISOR FROM pcmov,pcprodut, pcclient, pcusuari, pcsuperv WHERE pcmov.dtmov >= TRUNC(SYSDATE) -120 AND pcmov.codprod = pcprodut.codprod AND pcmov.codusur = pcusuari.codusur AND pcusuari.codsupervisor = pcsuperv.codsupervisor AND pcmov.codcli = pcclient.codcli AND pcmov.codfilial IN (1) AND pcmov.codoper = 'S'")

    lista = []
    for resultado in cur:
        lista.append(resultado)
    res_df = pd.DataFrame(lista)
    res_df_d = res_df.dropna()
    #print(res_df_d)
    #print(resultado)

    cur.close()
    con.close()

    return res_df_d


def query_produto():
    cur, con = conn_db()

    cur.execute("select pcprodut.codfornec,pcprodut.codprod,pcprodut.descricao,pcprodut.nbm ncm,pcprodut.codauxiliar ean,pcmarca.marca,pcprodut.embalagem,pcprodut.qtunitcx,pcprodut.pesoliq,pcprodut.codfab,pcprodut.codepto,pcdepto.descricao departamento,pcprodut.codsec,pcsecao.descricao secao,pcprincipativo.descricao principio_ativo from pcprodut, pcmarca, pcdepto, pcsecao, pcprincipativo, pcfornec where pcprodut.codmarca = pcmarca.codmarca and pcprodut.codepto = pcdepto.codepto and pcprodut.codsec = pcsecao.codsec and pcprodut.codfornec = pcfornec.codfornec and pcprodut.codprincipativo = pcprincipativo.codprincipativo(+)")

    lista = []
    for resultado in cur:
        lista.append(resultado)
    res_df = pd.DataFrame(lista)
    print(res_df)
    print(resultado)

    cur.close()
    con.close()

    return res_df


def query_fornecedor():
    cur, con = conn_db()

    cur.execute("SELECT pcfornec.codfornec, pcfornec.fornecedor, pcfornec.cgc CNPJ, pcfornec.ie INS_ESTADUAL from pcfornec where pcfornec.revenda = 'S'")

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
