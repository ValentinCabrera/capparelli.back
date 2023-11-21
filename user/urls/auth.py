from django.urls import path
from user.views.auth import LoginView, UserTokenView, MailCheckView, SignInView

urlpatterns = [
    path('log/', LoginView.as_view()),
    path('token/', UserTokenView.as_view()),
    path('mail/', MailCheckView.as_view()),
    path('sign/', SignInView.as_view()),
]