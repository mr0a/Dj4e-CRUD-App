from django.db import models
from django.core.validators import MinLengthValidator
from django.conf import settings

# Create your models here.
class Articles(models.Model):
    title = models.CharField(
        max_length=50,
        help_text = 'Enter title for your ad',
        validators = [MinLengthValidator(3, 'Enter title with minimum of 3 Characters')])
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.title