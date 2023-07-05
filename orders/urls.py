from django.urls import path
from .views import OrderView, OrderUpdateRetriverView

urlpatterns = [
    path("orders/", OrderView.as_view()),
    path("orders/<int:pk>/", OrderUpdateRetriverView.as_view()),
]
