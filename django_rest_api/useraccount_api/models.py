from django.db import models

# Create your models here.
class UserAccount(models.Model):
    email = models.TextField(unique=True)
    password = models.TextField()