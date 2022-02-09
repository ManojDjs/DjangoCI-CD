from rest_framework.serializers import ModelSerializer
from .models import User


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["last_login",
                  "is_superuser",
                  "is_staff",
                  "is_active",
                  "username",
                  "email",
                  "first_name",
                  "last_name"
                  ]


class UserRegSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",

        ]
