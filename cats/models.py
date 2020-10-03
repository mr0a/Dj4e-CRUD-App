from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Cats(models.Model):
    nickname = models.CharField(max_length=30)
    weight = models.PositiveIntegerField()
    foods = models.CharField(max_length = 100)
    breed = models.ForeignKey('Breeds', on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname


class Breeds(models.Model):
    name = models.CharField(
        max_length = 50,
        help_text = 'Enter a cat breed name',
        validators = [MinLengthValidator(2,"Enter name with more than 2 Characters")]
        )

    def __str__(self):
        return self.name