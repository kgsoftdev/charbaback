from django.db import models
from django.urls import reverse

from users.models import User

# Create your models here.

class TypeCharba(models.Model):
    type_charba = models.CharField(max_length=255)

    def __str__(self):
        return self.type_charba


class Charba(models.Model):
    type_charba = models.ForeignKey(TypeCharba, on_delete=models.CASCADE)
    code = models.IntegerField()
    code_chars = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_register = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type_charba}/{self.code}/{self.user}"

    def get_absolute_url(self):
        return reverse('list')

class CharbaUpdate(models.Model):
    mew_user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_update = models.DateTimeField()
    charba = models.ForeignKey(Charba, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.mew_user}/{self.date_update}/{self.charba}"