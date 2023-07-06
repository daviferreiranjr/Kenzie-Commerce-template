from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

# from .permissions import UserAdm, CustomUserPermission
from rest_framework import generics


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    queryset = User.objects.all()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]
    # permission_classes = [UserAdm or CustomUserPermission]

    queryset = User.objects.all()
