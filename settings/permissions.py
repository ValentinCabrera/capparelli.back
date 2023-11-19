from rest_framework.permissions import BasePermission
from back.permissions import CustomPermissionDenied
from .models import Setting

class IsOpen(BasePermission):
    message = "El local se encuentra cerrado."

    def has_permission(self, request, view):
        setting = Setting.get_setting()
        if not setting.is_open_now():
            raise CustomPermissionDenied(detail=self.message)

        return True
