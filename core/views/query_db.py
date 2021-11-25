import cx_Oracle
import pandas as pd
from core.views.get_data import register_log
from core.views.api_login import get_data_business


def conn_db():
    """
    Função responsável por conectar ao TNS do DB
    """
    business = get_data_business()
    con = cx_Oracle.connect(user=business.user_db, password=business.password_db, dsn=business.service_db)
    #con = cx_Oracle.connect(user="ESTRELA", password="star895thor", dsn="PROD")

    cur = con.cursor()
    print("CONECTOU ORACLE")

    return cur, con


def queryset_oracle(select_oracle):
    """
    Função responsável por realizar consultas ao banco oracle
    """
    try:
        
        cur, con = conn_db()
        cur.execute(select_oracle)

        lista_resultados = []
        for qs_db in cur:
            lista_resultados.append(qs_db)
        
        cur.close()
        con.close()

        df_resultados = pd.DataFrame(lista_resultados)
        #df_resultados = df_resultados.dropna()

        return df_resultados
    
    except:
        raise ValueError('Erro: Não foi possivel consultar o banco de dados')
