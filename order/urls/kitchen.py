from django.urls import path
from order.views.kitchen import (
    GetOrdersView,
    FinishOrderView
)


urlpatterns = [
    path('get/', GetOrdersView.as_view()),
    path('finish/', FinishOrderView.as_view()),
]