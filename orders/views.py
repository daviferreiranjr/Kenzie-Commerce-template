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

        # products_by_seller = {}

        # for product in products:
        #     seller_id = product.user_id

        #     if seller_id in products_by_seller:
        #         products_by_seller[seller_id].append(product)
        #     else:
        #         products_by_seller[seller_id] = [product]

        # client_email = order.user.email
        # subject = "Pedido realizado"
        # message = f"Olá {order.user.username}, seu pedido foi feito com sucesso.\n\nDetalhes do pedido:"

        # for seller_id, products in products_by_seller.items():
        #     message += f"\n\nProdutos do vendedor {products[0].user.username}:"
        #     for product in products:
        #         message += f"\n- {product.name} ({product.quantity})"

        # send_mail(
        #     subject,
        #     message,
        #     settings.DEFAULT_FROM_EMAIL,
        #     [client_email],
        #     fail_silently=False,
        # )


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
