import pandas as pd

from core.views.api_login import login_api
from core.models.providers import Provider
from core.models.products import Product
from core.models.histories import HistoryProduct
from core.models.sales import SaleProduct
from core.models.orders import OrdersBuy
from core.models.entries import EntryProduct
from core.models.stock import StockProduct
from core.views.send_to_data import send_data_integration
from core.views.process_query_data import (process_providers, process_products, process_sales, process_histories,
                                           process_orders, process_entries, process_stocks, process_order_duplicate)


def run_providers_task():
    token = login_api()
    df_providers = pd.DataFrame(Provider.objects.filter(sent=False).values())
    list_providers = process_providers(df_providers)
    url = "http://127.0.0.1:7000/api/integration/providers/"

    send_data_integration(url, token, list_providers)


def run_products_task():
    token = login_api()
    df_products = pd.DataFrame(Product.objects.filter(sent=False).values())
    list_products = process_products(df_products)

    url = "http://127.0.0.1:7000/api/integration/products/"
    send_data_integration(url, token, list_products)


def run_histories_task():
    token = login_api()
    df_histories = pd.DataFrame(HistoryProduct.objects.filter(sent=False).values())
    list_histories = process_histories(df_histories, False)
    url = "http://127.0.0.1:7000/api/integration/stock-histories/"

    send_data_integration(url, token, list_histories)


def run_sales_task():
    token = login_api()
    df_sales = pd.DataFrame(SaleProduct.objects.filter(sent=False).values())
    list_sales = process_sales(df_sales, False)
    url = "http://127.0.0.1:7000/api/integration/product-sales/"

    send_data_integration(url, token, list_sales)


def run_orders_task():
    token = login_api()
    df_orders = pd.DataFrame(OrdersBuy.objects.filter(sent=False).values())
    list_orders = process_orders(df_orders, False)
    url = "http://127.0.0.1:7000/api/integration/buy-orders/"

    send_data_integration(url, token, list_orders)


def run_orders_duplicate_task():
    token = login_api()
    df_orders_duplicate = pd.DataFrame(OrdersBuy.objects.filter(sent=False).values())
    list_orders_duplicate, id_company = process_order_duplicate(df_orders_duplicate)
    url_duplicates = f"http://127.0.0.1:7000/api/integration/orders-company/delete/{id_company}/"

    if len(list_orders_duplicate) != 0:
        send_data_integration(url_duplicates, token, list_orders_duplicate)

        remove_duplicate = OrdersBuy.objects.filter(order_number__in=list_orders_duplicate)
        remove_duplicate.delete()


def run_entries_task():
    token = login_api()
    df_entries = pd.DataFrame(EntryProduct.objects.filter(sent=False).values())
    list_entries = process_entries(df_entries, False)
    url = "http://127.0.0.1:7000/api/integration/entry-products/"

    send_data_integration(url, token, list_entries)


def run_stocks_task():
    token = login_api()
    df_stocks = pd.DataFrame(StockProduct.objects.filter(sent=False).values())
    list_stocks = process_stocks(df_stocks, False)
    url = "http://127.0.0.1:7000/api/integration/stock-current/"

    send_data_integration(url, token, list_stocks)
