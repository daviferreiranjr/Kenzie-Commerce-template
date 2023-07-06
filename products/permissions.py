from rest_framework import permissions
from users.models import User
from rest_framework.views import View
from products.models import Product


class IsSellerOrAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_seller or request.user.is_superuser
