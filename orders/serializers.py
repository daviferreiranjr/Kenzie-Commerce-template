from rest_framework import serializers
from .models import Order, ExpectedStatus
from cart.models import Cart

class OrderSerializer(serializers.ModelSerializer):

    status = serializers.ChoiceField(choices=ExpectedStatus.choices, default=ExpectedStatus.PEDIDO_REALIZADO)

    class Meta:
        model = Order
        fields = ["id", "user", "quantity", "status", "total_value", "created_at"]
        extra_kwargs = {
            "quantity": {"read_only": True},
            "total_value": {"read_only": True},
            "created_at": {"read_only": True},
            "user": {"read_only": True},
        }

    def create(self, validated_data): 
        user = validated_data["user"]
        cart = Cart.objects.get(user=user)
        validated_data['quantity'] = user.cart.products.count()
        validated_data['total_value'] = cart.total_value
        return Order.objects.create(**validated_data)

    
    def update(self, instance: Order, validated_data):
        instance.status = validated_data.get("status", instance.status)
        instance.save()
        return instance
