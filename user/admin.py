from django.contrib import admin
from .models import User
from django.utils.html import format_html

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "mail", "verificado", "is_staff"]

    def verificado(self, obj):
        if obj.is_checked():
            return format_html('<img src="/static/admin/img/icon-yes.svg" alt="True" title="True">')

        return format_html('<img src="/static/admin/img/icon-no.svg" alt="False" title="False">')