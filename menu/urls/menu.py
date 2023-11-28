from django.urls import path, include
from menu.views.menu import MenuView

urlpatterns = [
    path('', MenuView.as_view())
]