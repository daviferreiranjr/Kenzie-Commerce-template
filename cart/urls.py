from django.urls import path

from . import views

urlpatterns = [path("cart/", views.CartView.as_view()),
               path("cart/<str:user__username>/", views.CartDetailsView.as_view())]
