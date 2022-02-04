import datetime
import pandas as pd

from core.views.api_login import get_data_company
from core.views.get_data import get_providers_api, get_products_api, get_branches_api, get_orders_api, get_stock_api

from core.write_query_data.sale import writer_sale


def process_providers(df_providers, task=''):
    """  """
    if not df_providers.empty:

        df_providers.columns = ["cod_fornecedor", "desc_fornecedor", "cnpj", "iestadual"]
        company = get_data_company()
        df_providers['empresa'] = int(company.company_id)

        list_providers = get_providers_api(company.company_id)
        df_providers = df_providers.query("cod_fornecedor != @list_providers")

        if not task:
            dict_fornecedor = df_providers.assign(
                **df_providers.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict("records")

            return dict_fornecedor

        return df_providers

    else:
        raise ValueError('Erro: consulta ao banco de dados retornou vazia!')


def process_products(df_products, task=''):
    if not df_products.empty:

        df_products.columns = ["cod_fornecedor", "cod_produto", "desc_produto", "cod_ncm", "cod_auxiliar", "marca",
                               "embalagem", "quantidade_un_cx", "peso_liquido", "cod_fabrica", "cod_depto",
                               "desc_departamento", "cod_sec", "desc_secao", "principio_ativo"]

        company = get_data_company()
        df_products['empresa'] = company.company_id

        list_providers = get_providers_api(company.company_id)
        list_products = get_products_api(company.company_id)

        df_products = df_products.query("cod_fornecedor == @list_providers")
        df_products = df_products.query("cod_produto != @list_products")

        if not task:
            dict_products = df_products.assign(
                **df_products.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict(
                "records")

            return dict_products

        return df_products

    else:
        raise ValueError('Erro: consulta ao banco de dados retornou vazia!')


def process_histories(df_histories, task=''):
    if not df_histories.empty:

        df_histories.columns = ["cod_produto", "data", "qt_estoque", "cod_filial", "cod_fornecedor"]
        df_histories['data'] = pd.to_datetime(df_histories['data'])
        df_histories['cod_filial'] = df_histories['cod_filial'].astype(str).astype(int)

        company = get_data_company()
        df_histories['empresa'] = company.company_id

        list_providers = get_providers_api(company.company_id)
        list_products = get_products_api(company.company_id)
        list_branches = get_branches_api(company.company_id)

        df_histories = df_histories.query("cod_fornecedor == @list_providers")
        df_histories = df_histories.query("cod_produto == @list_products")
        df_histories = df_histories.query("cod_filial == @list_branches")

        if not task:
            dict_histories = df_histories.assign(
                **df_histories.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict(
                "records")

            return dict_histories

        return df_histories

    else:
        raise ValueError('Erro: consulta ao banco de dados retornou vazia!')


def process_sales(df_sales, task=''):
    if not df_sales.empty:
        df_sales.columns = ["data", "cod_produto", "qt_venda", "preco_unit", "cod_filial", "cliente", "num_nota",
                            "rca", "cod_fornecedor", "custo_fin", "supervisor"]
        df_sales['data'] = pd.to_datetime(df_sales['data'])
        df_sales['cod_filial'] = df_sales['cod_filial'].astype(str).astype(int)

        company = get_data_company()
        df_sales['empresa'] = company.company_id

        list_providers = get_providers_api(company.company_id)
        list_products = get_products_api(company.company_id)
        list_branches = get_branches_api(company.company_id)

        df_sales = df_sales.query("cod_fornecedor == @list_providers")
        df_sales = df_sales.query("cod_produto == @list_products")
        df_sales = df_sales.query("cod_filial == @list_branches")

        if not task:
            dict_sales = df_sales.assign(**df_sales.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict(
                "records")

            return dict_sales

        return df_sales

    else:
        raise ValueError('Erro: consulta ao banco de dados retornou vazia!')


def process_entries(df_entries, task=''):
    if not df_entries.empty:
        df_entries.columns = ["cod_filial", "data", "vl_ult_entrada", "qt_ult_entrada", "cod_produto",
                              "cod_fornecedor"]
        df_entries['data'] = pd.to_datetime(df_entries['data'])
        df_entries['cod_filial'] = df_entries['cod_filial'].astype(str).astype(int)

        company = get_data_company()
        df_entries['empresa'] = company.company_id

        list_providers = get_providers_api(company.company_id)
        list_products = get_products_api(company.company_id)
        list_branches = get_branches_api(company.company_id)

        df_entries = df_entries.query("cod_fornecedor == @list_providers")
        df_entries = df_entries.query("cod_produto == @list_products")
        df_entries = df_entries.query("cod_filial == @list_branches")

        if not task:
            dict_entries = df_entries.assign(
                **df_entries.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict("records")

            return dict_entries

        return df_entries

    else:
        raise ValueError('Erro: consulta ao banco de dados retornou vazia!')


def process_orders(df_orders, task=''):
    if not df_orders.empty:
        df_orders.columns = ["cod_filial", "cod_produto", "saldo", "num_pedido", "data", "cod_fornecedor"]
        df_orders['data'] = pd.to_datetime(df_orders['data'])
        df_orders['cod_filial'] = df_orders['cod_filial'].astype(str).astype(int)

        company = get_data_company()
        df_orders['empresa'] = company.company_id

        list_providers = get_providers_api(company.company_id)
        list_products = get_products_api(company.company_id)
        list_branches = get_branches_api(company.company_id)

        df_orders = df_orders.query("cod_fornecedor == @list_providers")
        df_orders = df_orders.query("cod_produto == @list_products")
        df_orders = df_orders.query("cod_filial == @list_branches")

        # list_orders, list_orders_products, list_orders_branches, list_orders_quantity_over, list_orders_date = get_orders_api(
        #     company.company_id, is_duplicated=True)
        #
        # df_orders = df_orders.query(
        #     "((cod_filial != @list_orders_branches and cod_produto != @list_orders_products) and (saldo != @list_orders_quantity_over and data != list_orders_date) and num_pedido != @list_orders)"
        # )


        if not task:
            dict_orders = df_orders.assign(**df_orders.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict(
                "records")

            return dict_orders

        return df_orders

    else:
        raise ValueError('Erro: consulta ao banco de dados retornou vazia!')


def process_order_duplicate(df_orders, task=''):
    if not df_orders.empty:
        df_orders.columns = ["cod_filial", "cod_produto", "saldo", "num_pedido", "data", "cod_fornecedor"]
        df_orders['data'] = pd.to_datetime(df_orders['data'])
        df_orders['cod_filial'] = df_orders['cod_filial'].astype(str).astype(int)

        company = get_data_company()
        df_orders['empresa'] = company.company_id

        list_orders = get_orders_api(company.company_id, is_duplicated=True)

        df_orders_duplicate = df_orders.query("num_pedido != @list_orders")

        if not task:
            dict_orders = df_orders_duplicate.assign(
                **df_orders_duplicate.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict(
                "records")

            return dict_orders, company.company_id

        return df_orders_duplicate

    else:
        raise ValueError('Erro: consulta ao banco de dados retornou vazia!')


def process_stocks(df_stock, task=''):
    if not df_stock.empty:

        df_stock.columns = ["cod_filial", "cod_produto", "qt_geral", "qt_indenizada", "qt_reservada",
                            "qt_pendente", "qt_bloqueada", "qt_disponivel", "custo_ult_entrada",
                            "cod_fornecedor", "preco_venda"]

        df_stock['data'] = datetime.date.today()
        df_stock['data'] = pd.to_datetime(df_stock['data'])
        df_stock['cod_filial'] = df_stock['cod_filial'].astype(str).astype(int)

        company = get_data_company()
        df_stock['empresa'] = company.company_id
        df_stock.fillna('0', inplace=True)

        list_providers = get_providers_api(company.company_id)
        list_products = get_products_api(company.company_id)
        list_branches = get_branches_api(company.company_id)

        df_stock = df_stock.query("cod_fornecedor == @list_providers")
        df_stock = df_stock.query("cod_produto == @list_products")
        df_stock = df_stock.query("cod_filial == @list_branches")

        if not task:

            # list_stock_produto, list_stock_filial, list_stock_qt_geral, list_stock_qt_disponivel, list_stock_preco = get_stock_api(
            #     company.company_id)

            # df_stock = df_stock.query(
            #     "(cod_filial != @list_stock_filial and cod_produto != @list_stock_produto) and (qt_geral != @list_stock_qt_geral and qt_disponivel != @list_stock_qt_disponivel)"
            # )

            dict_stock = df_stock.assign(
                **df_stock.select_dtypes(["datetime"]).astype(str).to_dict("list")).to_dict("records")

            return dict_stock

        return df_stock

    else:
        raise ValueError('Erro: consulta ao banco de dados retornou vazia!')
