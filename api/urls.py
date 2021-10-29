from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from .views import *

urlpatterns = [
    path('', access_valid, name='access_valid'),
    path('create-pedido/', create_pedido, name='create_pedido'),
    path('api-token-auth', views.obtain_auth_token, name='api-token-auth'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
