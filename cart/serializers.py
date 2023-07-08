from .models import Cart
from rest_framework import serializers
from users.models import User

from products.models import Product


class CartSerializerUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class CartSerializer(serializers.ModelSerializer):

    user = CartSerializerUser(read_only=True)

    def create(self, validated_data: Product) -> Cart:

        cart = Cart.objects.create()

        total_value = 0

        for product_data in validated_data["products"]:
            product = Product.objects.get(id=product_data.id)

            total_value += product.value

            cart.products.add(product)

        return Cart.objects.create(user=self.context["request"].user, total_value=total_value)

    def update(self, instance: Cart, validated_data: dict) -> Cart:
        products = validated_data.pop('products')

        for key, value in validated_data.items():
            setattr(instance, key, value)

        valor_total = 0

        for product in products:

            valor_total += product.value

        instance.total_value = valor_total

        instance.save()

        instance.products.set(products)

        return instance

    class Meta:
        model = Cart
        fields = ["id", "user", "products", "total_value"]
        extra_kwargs = {"id":  {"read_only": True},
                        "user": {"read_only": True},
                        "total_value": {"read_only": True}}
