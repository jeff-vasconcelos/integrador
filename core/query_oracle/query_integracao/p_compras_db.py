import pandas as pd


def p_compras_db():
    df_historico_pedidos = pd.read_csv('https://raw.githubusercontent.com/cluster-desenvolvimento/datasets/main/Pedido_Compras.csv', sep=';')
    return df_historico_pedidos
