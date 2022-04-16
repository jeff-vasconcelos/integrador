import cx_Oracle
import pandas as pd
from decouple import config


def conn_db():
    """
    Função responsável por conectar ao TNS do DB
    """
    con = cx_Oracle.connect(user=config('ORACLE_DB_USER'),
                            password=config('ORACLE_DB_PASSWORD'),
                            dsn=config('ORACLE_DB_DSN'))

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
        print(df_resultados)
        return df_resultados
    
    except:
        raise ValueError('Erro: Não foi possivel consultar o banco de dados')
