from django.db import models

class Address(models.Model):

    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    number = models.IntegerField()

    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        related_name="address",
    )
