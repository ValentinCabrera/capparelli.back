from rest_framework.permissions import BasePermission
from back.permissions import CustomPermissionDenied

class IsAdmin(BasePermission):
    message = "El token no pertenece a un admin."

    def has_permission(self, request, view):
        user = request.user

        if not user.is_staff:
            raise CustomPermissionDenied(detail=self.message)

        return True
