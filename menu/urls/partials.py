from django.urls import path
from back.utils import (get_active_view,
                        get_new_view,
                        get_alter_view,
                        get_inactive_view,
                        get_recover_view,
                        get_delete_view)

def get_abm_patterns(Model, Serializer):
    return [
        path('active/', get_active_view(Model, Serializer).as_view()),
        path('inactive/', get_inactive_view(Model, Serializer).as_view()),
        path('delete/', get_delete_view(Model, Serializer).as_view()),
        path('recover/', get_recover_view(Model, Serializer).as_view()),
        path('new/', get_new_view(Model, Serializer).as_view()),
        path('alter/', get_alter_view(Model, Serializer).as_view()),
    ]