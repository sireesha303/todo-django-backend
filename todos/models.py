"""
Models for todoapp
"""


from django.db import models
from django.contrib.auth import get_user_model
import uuid
from datetime import datetime

User = get_user_model()


class Todo(models.Model):
    """
    Todo Model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """String representation of the Todo model"""
        return self.title



