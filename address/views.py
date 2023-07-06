from .models import Address
from .serializers import AddressSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..users.permissions import IsAccountOwner


class AddressView(generics.CreateAPIView):
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]

    queryset = Address.objects.all()
