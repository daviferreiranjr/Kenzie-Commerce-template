from rest_framework import permissions
from rest_framework.views import Request, View

from users.models import User


class IsAdminOrSeller(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_superuser or request.user.is_seller


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_superuser


class IsCartOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User):
        return obj.id == request.user.id
