from rest_framework import permissions
from rest_framework.views import View
from .models import Order


class IsSellerPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Order) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user.is_seller and request.user == obj.user
