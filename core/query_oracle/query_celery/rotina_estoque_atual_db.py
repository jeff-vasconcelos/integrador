import pandas as pd


def estoque_atual_db():
    df_estoque_prod = pd.read_csv('https://raw.githubusercontent.com/cluster-desenvolvimento/news-datasets/main/Insight_Estoque.csv', sep=';')
    return df_estoque_prod
