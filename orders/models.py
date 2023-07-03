from django.db import models

class ExpectedStatus(models.TextChoices):
    PEDIDO_REALIZADO = "Pedido Realizado"
    EM_ANDAMENTO = "Em Andamento"
    ENTREGUE = "Entregue"

class Order(models.Model):

    quantity = models.IntegerField()
    status = models.CharField(max_length=50, choices=ExpectedStatus.choices, default=ExpectedStatus.PEDIDO_REALIZADO)
    created_at = models.DateField(auto_now_add=True)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="orders",
    )

    cart = models.OneToOneField(
        "cart.Cart",
        on_delete=models.CASCADE,
        related_name="cart",
    )
