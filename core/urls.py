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
    
    path('rotina/avarias/', rotina_avarias, name='avarias'),
    path('rotina/estoque-atual/', rotina_estoque_atual, name='estoque_atual'),
    path('rotina/hist-estoque/', rotina_hist_estoque, name='hist_estoque'),
    path('rotina/p-compras/', rotina_p_compras, name='p_compras'),
    path('rotina/ultima-entrada/', rotina_ultima_entrada, name='ultima_entrada'),
    path('rotina/vendas/', rotina_vendas, name='vendas'),

]
