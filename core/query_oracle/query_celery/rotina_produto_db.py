import pandas as pd


def produtos_db():
    df_produtos = pd.read_csv(
        'https://raw.githubusercontent.com/cluster-desenvolvimento/news-datasets/main/SKUs.csv',
        sep=';')
    return df_produtos
