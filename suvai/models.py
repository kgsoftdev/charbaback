from django.db import models
from users.models import User
from location.models import LocationVillage
from charbamodel.models import Charba


class Suvai(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    charba = models.ManyToManyField(Charba)
    date_start = models.DateField()
    date_end = models.DateField()
    price = models.IntegerField(default=0)
    suvachy = models.ForeignKey("Suvaichy", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date_start}/{self.date_end}"

class Suvaichy(models.Model):
    suvaichy = models.CharField(max_length=255)
    location = models.ForeignKey(LocationVillage, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)

    def __str__(self):
        return self.suvaichy