from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt import views as jwt_views
from .views import *

urlpatterns = [
    path('', access_valid, name='access_valid'),
    path('create-pedido', create_pedido, name='create_pedido'),
    path('status', teste, name='create_pedido'),
    path('token', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
