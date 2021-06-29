from django.urls import path
from core.query import *

urlpatterns = [
    path('teste/', conn_db, name='teste'),
]
