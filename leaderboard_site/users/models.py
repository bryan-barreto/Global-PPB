from django.db import models
import uuid

class UserProfile(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(default=" ", max_length=100)

