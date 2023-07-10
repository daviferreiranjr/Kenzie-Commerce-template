from rest_framework import generics

from .models import Cart
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import CartSerializer


class CartView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def perform_create(self, serializer):

        serializer.save(user=self.request.user)


class CartDetailsView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    lookup_field = "user__username"
