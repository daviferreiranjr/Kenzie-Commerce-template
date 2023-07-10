from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsSellerOrAdminPermission
from rest_framework import generics

# Create your views here.


class ProductView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOrAdminPermission]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        route_name_parameter = self.request.query_params.get("name", None)
        route_categoy_parameter = self.request.query_params.get(
            "category", None)

        if route_name_parameter:
            queryset = Product.objects.filter(
                name__icontains=route_name_parameter)
            return queryset

        if route_categoy_parameter:
            queryset = Product.objects.filter(
                category__icontains=route_categoy_parameter
            )
            return queryset

        return super().get_queryset()


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerOrAdminPermission]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
