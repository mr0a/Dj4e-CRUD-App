from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class crud(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)

class Make(models.Model):
    name = models.CharField(
        max_length = 50,
        help_text = "Enter a Maker (eg.BMW)",
        validators = [MinLengthValidator(3, "Must be greater than 2 Characters")])

    def __str__(self):
        return self.name

class Autos(models.Model):
    nickname = models.CharField(
        max_length = 50,
        validators = [MinLengthValidator(2, "Nickname must be greater than 1 character")])
    mileage = models.PositiveIntegerField()
    comments = models.CharField(max_length=300)
    make = models.ForeignKey('Make', on_delete = models.CASCADE, null = False)

    def __str__(self):
        return self.nickname