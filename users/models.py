from django.db import models
from django.contrib.auth.models import User, UserManager

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name='profile')
    balance = models.FloatField(max_length=9999999, default=0)
