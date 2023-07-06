from rest_framework import permissions
from users.models import User
from rest_framework.views import View


class IsSellerOrAdminPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        return (
            request.user.is_authenticated
            and request.user.is_seller
            and request.user == obj
            or request.user.is_superuser
        )
