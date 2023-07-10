from .models import Cart
from rest_framework import serializers
from users.models import User
from rest_framework.validators import UniqueValidator
from cart.models import Cart

from products.models import Product


class CartSerializerUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class CartSerializer(serializers.ModelSerializer):

    user = CartSerializerUser(read_only=True, validators=[
        UniqueValidator(queryset=Cart.user, message="cart already created.")])

    def create(self, validated_data: Product) -> Cart:

        total_value = 0
        print(validated_data["products"])

        for product_data in validated_data["products"]:
            # products = Product.objects.all().filter(id=product_data.id)
            test = Product.objects.get(id=product_data.id)
            # print("----------------------------------------")
            # print(products)

            # for product in products:

            #     print(product)

            total_value += test.value

        cart = Cart.objects.create(
            user=self.context["request"].user, total_value=total_value)
        cart.products.set(validated_data["products"])
        return cart

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
