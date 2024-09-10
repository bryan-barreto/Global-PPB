from django.db import models
import uuid
from datetime import datetime

class UserProfile(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uname = models.CharField(blank=False, max_length=100, editable=False, unique=True)
    pword_hash = models.CharField(blank=False, max_length=100, editable=True)
    birth_date = models.DateField(blank=True, null=True)
    favorite_stage = models.CharField(blank=True, max_length=1, null=True)
    acct_created = models.DateTimeField(blank=False, default=datetime.now())
    country = models.CharField(blank=True, max_length=100, editable=True, null=True)
    email = models.EmailField(blank=False, editable=True)
    
    def __str__(self) -> str:
        return f"{self.uname}"
    
    class Meta:
        db_table = 'players'


class Scores(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_uuid = models.ForeignKey(UserProfile, on_delete=models.CASCADE, db_column='user_uuid')
    score = models.FloatField(null=False)
    date = models.DateTimeField(blank=False, default=datetime.now())
    is_global = models.BooleanField(null=False, default=False, editable=True)
    
    def __str__(self) -> str:
        return f"{self.score}"
    
    class Meta:
        db_table = 'scores'