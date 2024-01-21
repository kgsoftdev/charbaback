from django.db import models

from users.models import User


# Create your models here.
class Reklama(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    theme = models.CharField(max_length=255)
    image = models.ImageField()
    date_create = models.DateTimeField()
    active = models.BooleanField(default=False)
    verify = models.BooleanField(default=False)
    price = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.theme}/{self.active}/{self.price}"