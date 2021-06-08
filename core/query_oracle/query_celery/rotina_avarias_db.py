#import cx_Oracle
import pandas as pd


def avarias_db():
    df_avaria = pd.read_csv('https://raw.githubusercontent.com/cluster-desenvolvimento/datasets/main/Avaria.csv', sep=';')
    return df_avaria
