from django.db import models

class ExpectedCategory(models.TextChoices):
    ALIMENTOS = "Alimentos"
    HIGIENE = "Higiene"
    BEBIDAS = "Bebidas"
    PRODUTOS_DE_BELEZA = "Produtos de Beleza"
    NAO_INFORMADO = "Não Informado"

class Product(models.Model):

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=ExpectedCategory.choices, default=ExpectedCategory.NAO_INFORMADO)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.IntegerField()

    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="products",
    )
