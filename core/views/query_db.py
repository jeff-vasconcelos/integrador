import cx_Oracle
import os
import pandas as pd
from core.views.get_data import register_log
from core.views.api_login import get_data_company


def conn_db():
    """
    Função responsável por conectar ao TNS do DB
    """
    # company = get_data_company()
    con = cx_Oracle.connect(user="BRASILMED",
                            password="BR4S1LM3D1",
                            dsn="PROD")

    cur = con.cursor()
    print("CONECTOU NO ORACLE")

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
