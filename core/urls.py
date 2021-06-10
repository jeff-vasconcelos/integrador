from django.urls import path
from core.views import *

urlpatterns = [
    path('', home, name='home'),
    path('integracao/avarias/', avarias, name='avarias'),
    path('integracao/estoque-atual/', estoque_atual, name='estoque_atual'),
    path('integracao/hist-estoque/', hist_estoque, name='hist_estoque'),
    path('integracao/p-compras/', p_compras, name='p_compras'),
    path('integracao/ultima-entrada/', ultima_entrada, name='ultima_entrada'),
    path('integracao/vendas/', vendas, name='vendas'),

]
