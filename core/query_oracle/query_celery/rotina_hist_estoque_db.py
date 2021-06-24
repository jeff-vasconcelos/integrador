import pandas as pd


def hist_estoque_db():
    df_historico_estoque = pd.read_csv('https://raw.githubusercontent.com/cluster-desenvolvimento/news-datasets/main/Insight_HistoricoEstoque.csv', sep=';')
    return df_historico_estoque
