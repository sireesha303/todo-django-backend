from rest_framework import serializers
from .models import *


class TodoSerializer(serializers.ModelSerializer):
    """
    Todo Model Serializer
    """

    class Meta:
        model = Todo
        fields = "__all__"

