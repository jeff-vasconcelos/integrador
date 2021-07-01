import cx_Oracle
import pandas as pd
from django.shortcuts import render

cx_Oracle.init_oracle_client(config_dir="/opt/oracle/instantclient_11_2/network/admin")


def conn_db(request, template_name='teste.html'):
    #nnota = 1 #698098
    #nfilial = 1
    con = cx_Oracle.connect(user="ESTRELA", password="star895thor", dsn="PROD")  # user, password, DNS
    cur = con.cursor()
    # cur.execute('select * from pcnfent where numnota = :nota', nota=nnota)
    cur.execute("select p.dtemissao, p.codfunc, b.nome as Comprador, p.numped, p.vltotal, p.obs from pcpedido p, pcempr b where p.dtemissao >= TRUNC(SYSDATE) - 0 and p.codfunc = b.matricula and p.codfunc in (273, 290)")
    #cur.execute('select column_name from dba_tab_cols')
    #cur.execute('select * from pcnfent p where p.numnota = :nota and p.codfilial = :filial', nota=nnota, filial=nfilial)
    #print(type(cur))
    lista = []
    for resultado in cur:
        lista.append(resultado)
    res_df = pd.DataFrame(lista)
    res_df_d = res_df.dropna()
    print(res_df_d)
    cur.close()
    con.close()

    return render(request, template_name)
