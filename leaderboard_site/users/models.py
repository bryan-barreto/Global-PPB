from django.db import models
import uuid

class UserProfile(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    uname = models.CharField(blank=False, max_length=100, editable=False)
    pword_hash = models.CharField(blank=False, max_length=100, editable=True)
    birth_date = models.DateField(blank=True)
    favorite_stage = models.CharField(blank=True, max_length=1)
    acct_created = models.DateTimeField(blank=False)
    country = models.CharField(blank=True, max_length=100, editable=True)
    
    def __str__(self) -> str:
        return f"{self.uname}"
    
    class Meta:
        db_table = 'player'
