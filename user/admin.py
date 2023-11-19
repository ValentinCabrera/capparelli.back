from django.contrib import admin
from .models import Client, Admin

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone_number']

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']
