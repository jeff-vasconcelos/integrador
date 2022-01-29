from django.urls import path
from core.views.single_integration_requests import (home_index, request_providers, request_products, request_histories,
                                                    request_sales, request_orders, request_entries, request_stock)

urlpatterns = [
    path('', home_index, name='home_index'),

    # Requisições AJAX
    path('request-fornecedores/', request_providers, name='request_providers'),
    path('request-produtos/', request_products, name='request_products'),
    path('request-historico/', request_histories, name='request_histories'),
    path('request-vendas/', request_sales, name='request_sales'),
    path('request-pedidos/', request_orders, name='request_orders'),
    path('request-entradas/', request_entries, name='request_entries'),
    path('request-estoque/', request_stock, name='request_stock'),
]
