from django.urls import path
from menu.views.category import *

urlpatterns = [
    path('active/', Active.as_view()),
    path('inactive/', Inactive.as_view()),
    path('delete/', Delete.as_view()),
    path('recover/', Recover.as_view()),
    path('new/', New.as_view()),
    path('alter/', Alter.as_view()),
]