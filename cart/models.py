from django.db import models


class Cart(models.Model):

    total_value = models.DecimalField(
        max_digits=8, decimal_places=2, null=True)

    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="cart",
        null=True
    )

    products = models.ManyToManyField(
        "products.Product",
        related_name="products"
    )