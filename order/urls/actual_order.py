from django.urls import path
from order.views.actual_order import GetOrderView


urlpatterns = [
    path('get/', GetOrderView.as_view()),
]