from .models import Address
from .serializers import AddressSerializer
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication


class AddressView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = AddressSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    serializer_class = AddressSerializer

    queryset = Address.objects.all()
