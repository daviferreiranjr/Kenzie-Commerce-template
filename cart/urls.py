from django.urls import path

from . import views

urlpatterns = [path("cart/", views.CartDetailView.as_view())]
