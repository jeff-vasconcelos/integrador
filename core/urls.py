from django.urls import path
from core.query import *
from core.views import ult_entrada, estoque, hist_estoque, p_compras, p_vendas , fornecedor, produto

urlpatterns = [
    path('ult-entrada/', ult_entrada, name='teste'),
    path('estoque/', estoque, name='teste'),
    path('hist-estoque/', hist_estoque, name='teste'),
    path('p-compras/', p_compras, name='teste'),
    path('p-vendas/', p_vendas, name='teste'),
    path('fornecedor/', fornecedor, name='teste'),
    path('produto/', produto, name='teste'),
]
