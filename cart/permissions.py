from rest_framework import permissions
from rest_framework.views import Request, View

# aqui fiquei em duvida em qual model usar no kwarg obj na IsCartOwner
from users.models import User
from .models import Cart


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_superuser


class IsCartOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Cart.user):
        return obj == request.user
