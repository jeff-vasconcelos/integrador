from django.urls import path
from core.views.integration_views import *

urlpatterns = [
    path('', home_index, name='home_index'),

    # Requisições AJAX
    path('request-fornecedores/', request_fornecedores, name='request_fornecedores'),
    path('request-produtos/', request_produtos, name='request_produtos'),
    path('request-historico/', request_historico, name='request_historico'),
    path('request-vendas/', request_vendas, name='request_vendas'),
    path('request-pedidos/', request_pedidos, name='request_pedidos'),
    path('request-entradas/', request_entradas, name='request_entradas'),
    path('request-estoque/', request_estoque, name='request_estoque'),
]
