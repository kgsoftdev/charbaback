from django.db import models
from django.contrib.auth.models import AbstractUser
from location.models import LocationVillage


class User(AbstractUser):
    user_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    avatar = models.ImageField()
    role_user = models.ForeignKey('RoleUser', on_delete=models.CASCADE, null=True)
    user_location = models.ForeignKey(LocationVillage, on_delete=models.CASCADE, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    EMAIL_FIELD = 'email'

    def __str__(self):
        return self.user_name
class RoleUser(models.Model):
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.role
