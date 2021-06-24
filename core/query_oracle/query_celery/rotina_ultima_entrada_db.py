import pandas as pd


def ultima_entrada_db():
    df_ultimas_entradas = pd.read_csv('https://raw.githubusercontent.com/cluster-desenvolvimento/news-datasets/main/Insight_Entrada.csv', sep=';')
    return df_ultimas_entradas
