from rest_framework import serializers
from .models import Product, ExpectedCategory


class ProductSerializer(serializers.ModelSerializer):
    category = serializers.ChoiceField(choices=ExpectedCategory.choices, default=ExpectedCategory.NAO_INFORMADO)
    available = serializers.SerializerMethodField()
    
    def get_available(self, obj: Product):
        stock = [product.stock for product in obj.all()]
        available = True
        if stock <= 0:
            available = False
        return available

    class Meta:
        model = Product
        fields = ["id", "name", "stock", "value", "available", "category", "user"]
        read_only_fields = ["id", "user"]

        def create(self, validated_data: dict) -> Product:
            return Product.objects.create(**validated_data)

        def update(self, instance: Product, validated_data: dict) -> Product:
            for key, value in validated_data.items():
                setattr(instance, key, value)

            return instance
