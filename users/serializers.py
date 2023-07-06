from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator


class UserSerializer(serializers.ModelSerializer):
    # depth = 2

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        is_superuser = validated_data.get("is_superuser")
        if is_superuser is not None:
            user = self.context["request"].user
            if not user.is_superuser:
                validated_data["is_superuser"] = instance.is_superuser

        password = validated_data.pop("password", None)
        instance = super().update(instance, validated_data)

        if password:
            instance.set_password(password)

        instance.save()
        return instance

    email = serializers.EmailField(
        validators=[UniqueValidator(User.objects.all(), "This field must be unique.")]
    )

    class Meta:
        model = User
        fields = ["id", "username", "password", "email", "is_seller", "is_superuser"]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_superuser": {"read_only": True},
        }
