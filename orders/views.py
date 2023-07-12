from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import OrderSerializer
from .models import Order
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsSellerPermission
from django.core.mail import send_mail
from django.conf import settings


class OrderView(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        order = serializer.save(user=self.request.user)

class OrderUpdateRetriverView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsSellerPermission]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_update(self, serializer):
        order = self.get_object()

        serializer.save()
        if serializer.instance.status != order.status:
            subject = "Pedido atualizado"
            message = (
                f"Olá {order.user.username}, o status do seu pedido foi atualizado."
            )
            message += f"Novo status:{order.status}"

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [order.user.email],
                fail_silently=False,
            )
