from django.contrib import admin
from .models import User, Client, Admin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'get_user_group']

    def get_user_group(self, obj):
        return obj.get_user_group()

    get_user_group.short_description = "Group"


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone_number']

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'phone_number']

