from django.urls import path, include
from .views import *

app_name = 'order'

urlpatterns = [
    path('current/', include('order.urls.current_order')),
    path('kitchen/', include('order.urls.kitchen')),
    path('lounge/', include('order.urls.lounge'))
]