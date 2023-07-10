from rest_framework import permissions
from .models import Address
from rest_framework.views import View, Request

    
class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Address):
        return obj.user.id == request.user.id

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_superuser