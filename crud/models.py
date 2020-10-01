from django.db import models

# Create your models here.
class crud(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)