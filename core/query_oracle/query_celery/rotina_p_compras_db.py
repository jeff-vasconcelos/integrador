import pandas as pd


def p_compras_db():
    df_pedidos_compras = pd.read_csv('https://raw.githubusercontent.com/cluster-desenvolvimento/news-datasets/main/Insight_PedidoCompras.csv', sep=';')
    return df_pedidos_compras
