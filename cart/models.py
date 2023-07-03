from django.db import models

class Cart(models.Model):

    total_value = models.FloatField()

    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="cart",
    )

    products = models.ManyToManyField(
        "products.Product",
        related_name="products",
    )