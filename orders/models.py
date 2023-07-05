from django.db import models


class ExpectedStatus(models.TextChoices):
    PEDIDO_REALIZADO = "Pedido Realizado"
    EM_ANDAMENTO = "Em Andamento"
    ENTREGUE = "Entregue"
    CANCELADO = "Cancelado"


class Order(models.Model):
    quantity = models.IntegerField()
    status = models.CharField(
        max_length=50,
        choices=ExpectedStatus.choices,
        default=ExpectedStatus.PEDIDO_REALIZADO,
    )
    total_value = models.FloatField()
    created_at = models.DateField(auto_now_add=True)

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="orders",
    )
