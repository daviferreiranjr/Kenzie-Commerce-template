from rest_framework import permissions
from .models import Product
from rest_framework.views import View



class IsSellerOrAdminPermission(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Product) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return (
            request.user.is_seller and request.user == obj
        )
    
    def has_permission(self, request, view: View) -> bool:
        return (
            request.user.is_authenticated
            and request.user.is_superuser
        )