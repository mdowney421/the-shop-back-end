from django.db import models

# Create your models here.
class InventoryItem(models.Model):
    image = models.TextField()
    title = models.TextField()
    description = models.TextField()
    price = models.IntegerField()