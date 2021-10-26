import cx_Oracle
import pandas as pd
from core.views.get_data import get_data_business, register_log


def conn_db():
    """
    Função responsável por conectar ao TNS do DB
    """
    business = get_data_business()
    con = cx_Oracle.connect(user=business.user_db, password=business.password_db, dsn=business.service_db)
    cur = con.cursor()

    return cur, con


def queryset_oracle(select_oracle):
    """
    Função responsável por realizar consultas ao banco oracle
    """

    cur, con = conn_db()
    cur.execute(select_oracle)

    try:

        lista_resultados = []
        for qs_db in cur:
            lista_resultados.append(qs_db)

        df = pd.DataFrame(lista_resultados)
        df_resultados = df.dropna()

        cur.close()
        con.close()

        return df_resultados
    except NameError as err:
        erro = str(err)
        register_log(f"Error: {erro}")
