from rest_framework import generics
from .models import Cart
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import CartSerializer
from .permissions import IsAdmin, IsCartOwner


class CartView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdmin | IsCartOwner]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
