from django.urls import path
from order.views.lounge import GetOrdersView


urlpatterns = [
    path('get/', GetOrdersView.as_view()),
]