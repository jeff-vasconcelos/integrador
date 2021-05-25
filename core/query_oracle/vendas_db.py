import pandas as pd


def vendas_db():
    df_historico_vendas = pd.read_csv('https://raw.githubusercontent.com/cluster-desenvolvimento/datasets/main/Venda.csv', sep=';')
    return df_historico_vendas
