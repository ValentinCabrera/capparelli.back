from django.urls import path
from user.views.auth import LoginView, UserTokenView, MailCheckView, SignInView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('check_token/', UserTokenView.as_view()),
    path('check_mail/', MailCheckView.as_view(),),
    path('signin/', SignInView.as_view()),
]