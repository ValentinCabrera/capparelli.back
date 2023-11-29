from django.urls import path
from order.views.current_order import (
    GetOrderView,
    AddItemView,
    AddDiscountView,
    DeleteItemView,
    OrderToKitchenView)


urlpatterns = [
    path('get/', GetOrderView.as_view()),
    path('add/', AddItemView.as_view()),
    path('discount/', AddDiscountView.as_view()),
    path('delete/', DeleteItemView.as_view()),
    path('kitchen/', OrderToKitchenView.as_view())
]