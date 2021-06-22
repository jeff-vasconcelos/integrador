import pandas as pd


def vendas_db():
    df_historico_vendas = pd.read_csv('https://raw.githubusercontent.com/cluster-desenvolvimento/news-datasets/main/Insight_Vendas.csv', sep=';')
    return df_historico_vendas
