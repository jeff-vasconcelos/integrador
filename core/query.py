import cx_Oracle
import pandas as pd


def conn_db():
    con = cx_Oracle.connect(user="ESTRELA", password="star895thor", dsn="PROD")  # user, password, DNS
    cur = con.cursor()

    return cur, con


def query_ult_entrada():

    cur, con = conn_db()

    cur.execute('SELECT pcest.codfilial, pcest.dtultent, pcest.valorultent, pcest.qtultent QTD_ULT_ENTRADA,pcprodut.codprod , pcprodut.descricao FROM pcest, pcprodut WHERE pcest.dtultent >= TRUNC(SYSDATE) -400 AND pcprodut.codprod = pcest.codprod AND pcest.codfilial IN (1)')

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

    cur.execute('SELECT pcprodut.descricao, pcprodut.embalagem, pcest.codfilial, pcest.codprod, pcest.qtestger, pcest.qtindeniz, pcest.qtreserv, pcest.qtpendente, pcest.qtbloqueada, pcest.qtestger - (pcest.qtindeniz + pcest.qtreserv + pcest.qtpendente + pcest.qtbloqueada) AS Qtd_Disp, pcest.custoultent, pcfornec.codfornec, pcfornec.fornecedor, pctabpr.pvenda FROM pcprodut, pcest, pcfornec, pctabpr WHERE pcest.codprod = pcprodut.codprod AND pcprodut.codprod = pctabpr.codprod AND pcprodut.codfornec = pcfornec.codfornec AND pcest.codfilial in (1) AND pctabpr.numregiao = 1')

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

    cur.execute('SELECT pchistest.codprod, pcprodut.descricao, pcprodut.embalagem, pchistest.data, pchistest.qtestger, pchistest.codfilial FROM pchistest, pcprodut WHERE pchistest.codprod = pcprodut.codprod AND pchistest.data >= TRUNC(SYSDATE) -120 AND pchistest.codfilial in (1) ORDER BY pchistest.codfilial, pchistest.codprod, pchistest.data')

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

    cur.execute('SELECT pcpedido.codfilial, pcitem.codprod, pcprodut.descricao, pcitem.qtpedida - pcitem.qtentregue AS SALDO, pcitem.numped, pcpedido.dtemissao FROM pcprodut, pcitem, pcpedido WHERE pcitem.codprod = pcprodut.codprod AND pcitem.numped = pcpedido.numped AND pcpedido.dtemissao >= TRUNC(SYSDATE) - 120')

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

    cur.execute("SELECT PCMOV.DTMOV, PCPRODUT.CODPROD, PCPRODUT.DESCRICAO, PCMOV.QT, PCMOV.PUNIT, PCMOV.CODFILIAL, PCCLIENT.CLIENTE, PCMOV.CODEPTO, PCDEPTO.DESCRICAO DEPARTAMENTO, PCMOV.NUMNOTA, PCMOV.CODUSUR, PCMOV.CODFORNEC, PCSECAO.DESCRICAO SECAO, PCMOV.CUSTOFIN, PCMOV.PUNIT, PCPRINCIPATIVO.DESCRICAO PRINCIPIO_ATIVO FROM PCMOV, PCDEPTO, PCPRODUT, PCSECAO, PCCLIENT, PCPRINCIPATIVO WHERE DTMOV >= TRUNC(SYSDATE) - 120 AND PCMOV.CODEPTO = PCDEPTO.CODEPTO AND PCMOV.CODPROD = PCPRODUT.CODPROD AND PCPRODUT.CODPRINCIPATIVO = PCPRINCIPATIVO.CODPRINCIPATIVO (+) AND PCPRODUT.CODSEC = PCSECAO.CODSEC AND PCMOV.CODCLI = PCCLIENT.CODCLI AND PCMOV.CODFILIAL IN (1) AND PCMOV.CODOPER = 'S'")

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


def query_produto():
    cur, con = conn_db()

    cur.execute("select pcprodut.codfornec,pcprodut.codprod,pcprodut.descricao,pcprodut.nbm ncm,pcprodut.codauxiliar ean,pcmarca.marca,pcprodut.embalagem,pcprodut.qtunitcx,pcprodut.pesoliq,pcprodut.codfab,pcprodut.codepto,pcdepto.descricao departamento,pcprodut.codsec,pcsecao.descricao secao,pcprincipativo.descricao principio_ativo from pcprodut, pcmarca, pcdepto, pcsecao, pcprincipativo, pcfornec where pcprodut.codmarca = pcmarca.codmarca and pcprodut.codepto = pcdepto.codepto and pcprodut.codsec = pcsecao.codsec and pcprodut.codfornec = pcfornec.codfornec and pcprodut.codprincipativo = pcprincipativo.codprincipativo(+)")
    #cur.execute("select pcrodut.codprod , pcprodut.descricao, pcprodut.nbm, pcprodut.codauxiliar,pcmarca.marca,pcprodut.embalagem,pcprodut.qtunitcx,pcprodut.pesoliq,pcprodut.codfab,pcprodut.codepto,pcdepto.descricao,pcprodut.codsec,pcsecao.descricao from pcprodut, pcmarca, pcdepto, pcsecao where pcprodut.codmarca = pcmarca.codmarca and pcprodut.codepto = pcdepto.codepto and pcprodut.codsec = pcsecao.codsec")

    lista = []
    for resultado in cur:
        lista.append(resultado)
    res_df = pd.DataFrame(lista)
    #res_df_d = res_df.dropna()
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
