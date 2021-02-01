from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=75)
    price = models.DecimalField(max_digits=5, decimal_places=2)
