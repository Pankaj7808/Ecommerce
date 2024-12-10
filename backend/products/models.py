from django.db import models
from django.contrib.auth.models import AbstractUser


class Product(models.Model):
    name = models.CharField(max_length=10)
    description = models.TextField()
    price = models.IntegerField()
    category = models.CharField(max_length=50)
    quantity = models.IntegerField()
    is_active = models.BooleanField()