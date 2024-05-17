from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
   title = models.CharField(max_length=200)
   post = models.TextField() 
   created_at = models.DateTimeField(default = timezone.now) 

# Create your models here.
class User(models.Model):
   firstname = models.CharField(max_length=200)
   lastname = models.CharField(max_length=200)
   email = models.CharField(max_length=200)
   password = models.CharField(max_length=200)
   created_at = models.DateTimeField(default = timezone.now)