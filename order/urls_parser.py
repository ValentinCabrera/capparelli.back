from django.urls import path, include
from .views import *

app_name = 'order'

urlpatterns = [
    path('actual/', include('order.urls.actual_order')),
]