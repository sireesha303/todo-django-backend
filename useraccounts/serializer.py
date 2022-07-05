from rest_framework import serializers
from .models import *

from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer for custom user model
    """

    class Meta:
        model = CustomUser
        fields = "__all__"


