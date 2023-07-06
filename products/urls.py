from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path("products/", views.ProductView.as_view()),
    path("products/<int:pk>/", views.ProductDetailView.as_view()),
]