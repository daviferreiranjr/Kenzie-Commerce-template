from rest_framework import serializers
from .models import Order
from cart.models import Cart


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model: Order
        fields: "__all__"

    def create(self, validated_data: Cart, user_id):
        return Order.objects.create(
            total_value=validated_data.total_value,
            user=user_id,
            quantity=validated_data.products.count,
        )

    def update(self, instance: Order, validated_data):
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        return instance
