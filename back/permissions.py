from rest_framework.exceptions import PermissionDenied
class CustomPermissionDenied(PermissionDenied):
    def __init__(self, detail):
        self.detail = detail