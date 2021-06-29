import cx_Oracle
from django.shortcuts import render

cx_Oracle.init_oracle_client(config_dir="/opt/oracle/instantclient_11_2/network/admin")


def conn_db(request, template_name='teste.html'):
    nnota = 1  # 698098
    nfilial = 1
    con = cx_Oracle.connect(user="ESTRELA", password="star895thor", dsn="PROD")  # user, password, DNS
    cur = con.cursor()
    cur.execute('select * from pcnfent where numnota = :nota', nota=nnota)
    # cur.execute('select * from pcnfent p where p.numnota = :nota and p.codfilial = :filial', nota=nnota, filial=nfilial)
    for resultado in cur:
        print(resultado)
    cur.close()
    con.close()

    return render(request, template_name)
