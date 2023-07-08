from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["id", "state", "city", "neighborhood", "street", "number", "user"]
        read_only_fields = ["id", "user"]

    def create(self, validated_data):
        return Address.objects.create(**validated_data)
