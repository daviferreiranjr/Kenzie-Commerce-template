from rest_framework import permissions
from rest_framework.views import View
from orders.models import Order


class AuthenticationSeller(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Order):
        products = obj.products.all()
        sellers = set([product.user_id for product in products])

        return request.user.id in sellers
