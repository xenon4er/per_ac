from django.db import models
from django.contrib.auth.models import User
# Create your models here.
    
class Category(models.Model):
    Title = models.CharField(max_length = 255)
    periodicity = models.IntegerField(max_length = 10)
    FK_User = models.ForeignKey(User)
    def __unicode__(self):
        return self.Title

class Safe(models.Model):
    Title = models.CharField(max_length = 255)
    FK_User = models.ForeignKey(User)
    def __unicode__(self):
        return self.Title

class Payment(models.Model):
    FK_User = models.ForeignKey(User)
    currency = models.CharField(max_length = 10)
    Reason = models.CharField(max_length = 255)
    Amount_of_payment = models.FloatField(max_length = 50)
    date = models.DateField()
    FK_Category = models.ForeignKey(Category)
    Fk_Safe = models.ForeignKey(Safe)
    def __unicode__(self):
        return self.Amount_of_payment
