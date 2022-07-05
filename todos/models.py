"""
Models for todoapp
"""


from django.db import models
from django.contrib.auth import get_user_model
import uuid

User = get_user_model()


class Todo(models.Model):
    """
    Todo Model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    status = models.BooleanField(default=False);
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        """String representation of the Todo model"""
        return self.title
