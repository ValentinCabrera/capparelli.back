from django.urls import path
from order.views.actual_order import GetOrderView, AddItemView


urlpatterns = [
    path('get/', GetOrderView.as_view()),
    path('add/', AddItemView.as_view())
]