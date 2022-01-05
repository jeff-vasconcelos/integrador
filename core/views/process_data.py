import datetime
import pandas as pd

from core.views.api_login import get_data_business
from core.views.get_data import *


def process_fornecedores(df_fornecedores):
    """  """
    if not df_fornecedores.empty:
        df_fornecedores.columns = ["cod_fornecedor", "desc_fornecedor", "cnpj", "iestadual"]
        business = get_data_business()
        df_fornecedores['empresa'] = int(business.empresa_id)

        dict_fornecedor = df_fornecedores.assign(
            **df_fornecedores.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict("records")

        return dict_fornecedor

    else:
        raise ValueError('Erro: consulta ao banco de dados retornou vazia!')      


def process_produtos(df_produtos, integration=''):
    if not df_produtos.empty:

        df_produtos.columns = ["cod_fornecedor", "cod_produto", "desc_produto", "cod_ncm", "cod_auxiliar", "marca",
                               "embalagem", "quantidade_un_cx", "peso_liquido", "cod_fabrica", "cod_depto",
                               "desc_departamento", "cod_sec", "desc_secao", "principio_ativo"]

        business = get_data_business()
        df_produtos['empresa'] = business.empresa_id

        if integration:
            lista_fornecedores = get_fornecedores_api(business.empresa_id)
            df_produtos = df_produtos.query("cod_fornecedor == @lista_fornecedores")

        dict_produtos = df_produtos.assign(
            **df_produtos.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict(
            "records")

        return dict_produtos

    else:
        raise ValueError('Erro: consulta ao banco de dados retornou vazia!')


def process_historico(df_historico, integration=''):
    if not df_historico.empty:
        df_historico.columns = ["cod_produto", "data", "qt_estoque", "cod_filial", "cod_fornecedor"]
        df_historico['data'] = pd.to_datetime(df_historico['data'])
        df_historico['cod_filial'] = df_historico['cod_filial'].astype(str).astype(int)

        business = get_data_business()
        df_historico['empresa'] = business.empresa_id

        if integration:
            lista_fornecedores = get_fornecedores_api(business.empresa_id)
            lista_produtos = get_produtos_api(business.empresa_id)
            lista_filial = get_filial_api(business.empresa_id)

            df_historico = df_historico.query("cod_fornecedor == @lista_fornecedores")
            df_historico = df_historico.query("cod_produto == @lista_produtos")
            df_historico = df_historico.query("cod_filial == @lista_filial")

        dict_historico = df_historico.assign(
            **df_historico.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict(
            "records")

        return dict_historico

    else:
        raise ValueError('Erro: consulta ao banco de dados retornou vazia!')


def process_vendas(df_vendas, integration=''):
    if not df_vendas.empty:
        df_vendas.columns = ["data", "cod_produto", "qt_venda", "preco_unit", "cod_filial", "cliente", "num_nota",
                             "rca", "cod_fornecedor", "custo_fin", "supervisor"]
        df_vendas['data'] = pd.to_datetime(df_vendas['data'])
        df_vendas['cod_filial'] = df_vendas['cod_filial'].astype(str).astype(int)

        business = get_data_business()
        df_vendas['empresa'] = business.empresa_id

        if integration:
            lista_fornecedores = get_fornecedores_api(business.empresa_id)
            lista_produtos = get_produtos_api(business.empresa_id)
            lista_filial = get_filial_api(business.empresa_id)

            df_vendas = df_vendas.query("cod_fornecedor == @lista_fornecedores")
            df_vendas = df_vendas.query("cod_produto == @lista_produtos")
            df_vendas = df_vendas.query("cod_filial == @lista_filial")

        dict_vendas = df_vendas.assign(**df_vendas.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict(
            "records")

        return dict_vendas

    else:
        raise ValueError('Erro: consulta ao banco de dados retornou vazia!')


def process_entradas(df_entrada, integration=''):
    if not df_entrada.empty:
        df_entrada.columns = ["cod_filial", "data", "vl_ult_entrada", "qt_ult_entrada", "cod_produto",
                              "cod_fornecedor"]
        df_entrada['data'] = pd.to_datetime(df_entrada['data'])
        df_entrada['cod_filial'] = df_entrada['cod_filial'].astype(str).astype(int)

        business = get_data_business()
        df_entrada['empresa'] = business.empresa_id

        if integration:
            lista_fornecedores = get_fornecedores_api(business.empresa_id)
            lista_produtos = get_produtos_api(business.empresa_id)
            lista_filial = get_filial_api(business.empresa_id)

            df_entrada = df_entrada.query("cod_fornecedor == @lista_fornecedores")
            df_entrada = df_entrada.query("cod_produto == @lista_produtos")
            df_entrada = df_entrada.query("cod_filial == @lista_filial")

        dict_entradas = df_entrada.assign(
            **df_entrada.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict("records")

        return dict_entradas

    else:
        raise ValueError('Erro: consulta ao banco de dados retornou vazia!')


def process_pedidos(df_pedidos, integration=''):
    if not df_pedidos.empty:
        df_pedidos.columns = ["cod_filial", "cod_produto", "saldo", "num_pedido", "data", "cod_fornecedor"]
        df_pedidos['data'] = pd.to_datetime(df_pedidos['data'])
        df_pedidos['cod_filial'] = df_pedidos['cod_filial'].astype(str).astype(int)

        business = get_data_business()
        df_pedidos['empresa'] = business.empresa_id

        if integration:
            lista_fornecedores = get_fornecedores_api(business.empresa_id)
            lista_produtos = get_produtos_api(business.empresa_id)
            lista_filial = get_filial_api(business.empresa_id)

            df_pedidos = df_pedidos.query("cod_fornecedor == @lista_fornecedores")
            df_pedidos = df_pedidos.query("cod_produto == @lista_produtos")
            df_pedidos = df_pedidos.query("cod_filial == @lista_filial")

        dict_pedido = df_pedidos.assign(**df_pedidos.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict(
            "records")

        return dict_pedido

    else:
        raise ValueError('Erro: consulta ao banco de dados retornou vazia!')


def process_estoque(df_estoque, integration=''):
    if not df_estoque.empty:

        df_estoque.columns = ["cod_filial", "cod_produto", "qt_geral", "qt_indenizada", "qt_reservada",
                              "qt_pendente", "qt_bloqueada", "qt_disponivel", "custo_ult_entrada",
                              "cod_fornecedor", "preco_venda"]

        df_estoque['data'] = datetime.date.today()
        df_estoque['data'] = pd.to_datetime(df_estoque['data'])
        df_estoque['cod_filial'] = df_estoque['cod_filial'].astype(str).astype(int)

        business = get_data_business()
        df_estoque['empresa'] = business.empresa_id
        df_estoque.fillna('0', inplace=True)

        if integration:
            lista_fornecedores = get_fornecedores_api(business.empresa_id)
            lista_produtos = get_produtos_api(business.empresa_id)
            lista_filial = get_filial_api(business.empresa_id)

            df_estoque = df_estoque.query("cod_fornecedor == @lista_fornecedores")
            df_estoque = df_estoque.query("cod_produto == @lista_produtos")
            df_estoque = df_estoque.query("cod_filial == @lista_filial")

        dict_estoque = df_estoque.assign(
            **df_estoque.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict("records")

        return dict_estoque

    else:
        raise ValueError('Erro: consulta ao banco de dados retornou vazia!')
