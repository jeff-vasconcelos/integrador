import cx_Oracle
import pandas as pd
from django.shortcuts import render

cx_Oracle.init_oracle_client(config_dir="/opt/oracle/instantclient_11_2/network/admin")


def conn_db(request, template_name='teste.html'):
    nnota = 1 #698098
    nfilial = 1
    con = cx_Oracle.connect(user="ESTRELA", password="star895thor", dsn="PROD")  # user, password, DNS
    cur = con.cursor()
    '''
    Mostrar todas as linhas e colunas
    
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    '''
    pd.set_option('display.max_rows', None)
    # cur.execute('select * from pcnfent where numnota = :nota', nota=nnota)
    #cur.execute("select column_name from all_tab_cols where table_name = 'pcprodut'")
    #cur.execute("select p.dtemissao, p.codfunc, b.nome as Comprador, p.numped, p.vltotal, p.obs from pcpedido p, pcempr b where p.dtemissao >= TRUNC(SYSDATE) - 0 and p.codfunc = b.matricula and p.codfunc in (273, 290)")
    cur.execute('SELECT pcest.codfilial, pcest.dtultent, pcest.valorultent, pcest.qtultent QTD_ULT_ENTRADA, pcprodut.codprod , pcprodut.descricao FROM pcest, pcprodut WHERE pcest.dtultent >= TRUNC(SYSDATE) -400 AND pcprodut.codprod = pcest.codprod AND pcest.codfilial IN (1)')
    #cur.execute('select pcmov.codprod, pcprodut.descricao from pcmov, pcprodut where pcmov.dtmov >= TRUNC(SYSDATE) - 0 and pcmov.codprod = 20 pcmov.codprod = pcprodut.codprod')
    #cur.execute('select * from pcnfent p where p.numnota = :nota and p.codfilial = :filial', nota=nnota, filial=nfilial)
    #print(type(cur))
    lista = []
    for resultado in cur:
        lista.append(resultado)
    res_df = pd.DataFrame(lista)
    res_df_d = res_df.dropna()
    print(res_df_d.info())
    print(resultado)

    cur.close()
    con.close()

    return render(request, template_name)
