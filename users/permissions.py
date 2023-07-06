# from rest_framework import permissions
# from .models import User
# from rest_framework.views import View

    
# class UserAdm(permissions.BasePermission):
#     def has_permission(self, request, view):
#         user = request.user
#         return user.is_authenticated and user.is_superuser
    
# class CustomUserPermission(permissions.BasePermission):
#     def has_permission(self, request, view: View, obj: User):
#         if not request.user.is_authenticated:
#             return False

#         if request.user.is_seller:
#             return True
        
#         if request.user.is_superuser:
#             return True
        
#         return request.user.is_authenticated and obj == request.user