from django.db import models

# Create your models here.
class Cart(models.Model):
    image = models.TextField()
    title = models.TextField()
    description = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()
