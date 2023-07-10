from rest_framework import permissions
from .models import Product
from rest_framework.views import View


class IsSellerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Product) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_seller and request.user == obj.user


class IsAdminPermission(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_superuser