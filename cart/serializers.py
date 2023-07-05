from .models import Cart
from rest_framework import serializers


class CartSerializer(serializers.ModelSerializer):

    def create(self, validated_data: dict) -> Cart:
        return Cart.objects.create(**validated_data)

    def update(self, instance: Cart, validated_data: dict) -> Cart:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()
        return instance

    class Meta:
        model = Cart
        fields = ["id", "total_value", "user", "products"]
        extra_kwargs = {"id":  {"read_only": True},
                        "products": {"read_only": True}}
