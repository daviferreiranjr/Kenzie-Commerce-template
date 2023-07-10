from .models import Address
from .serializers import AddressSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAccountOwner, IsAdmin


class AddressView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner]
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwner or IsAdmin]
    serializer_class = AddressSerializer

    queryset = Address.objects.all()
