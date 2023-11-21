from django.urls import path
from user.views.auth import LoginView, UserTokenView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('token/', UserTokenView.as_view()),
]