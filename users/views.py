from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
# from .permissions import UserAdm, CustomUserPermission
from rest_framework import generics

class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [UserAdm or CustomUserPermission]

    queryset = User.objects.all()
