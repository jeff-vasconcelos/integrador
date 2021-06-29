import cx_Oracle
cx_Oracle.init_oracle_client(config_dir="/opt/oracle/instantclient_11_2/network/admin")

nnota = int(input('Digite o numero da NF: '))
filial = int(input('Digite o numero da Filial: '))


def connect():
    con = cx_Oracle.connect(user="ESTRELA", password="star895thor", dsn="PROD")  #user, password, DNS
    cur = con.cursor()
    cur.execute('select * from pcnfent p where p.numnota = :nota and p.codfilial = :nfilial', nota=nnota, nfilial=filial)
    for resultado in cur:
        print(resultado)
    cur.close()
    con.close()
