from django.db import models


# Create your models here.
class LoationCountry(models.Model):
    name_country = models.CharField(max_length=255)

    def __str__(self):
        return self.name_country


class LocationOblast(models.Model):
    id_conutry = models.ForeignKey(LoationCountry, on_delete=models.CASCADE)
    name_oblast = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id_conutry} | {self.name_oblast}"


class LocationRegion(models.Model):
    id_oblast = models.ForeignKey(LocationOblast, on_delete=models.CASCADE)
    name_region = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id_oblast} | {self.name_region}"


class LocationOkmot(models.Model):
    id_region = models.ForeignKey(LocationRegion, on_delete=models.CASCADE)
    name_okmot = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.id_region} | {self.name_okmot}"


class LocationVillage(models.Model):
    id_okmot = models.ForeignKey(LocationOkmot, on_delete=models.CASCADE, verbose_name="Айыл окмот")
    name_village = models.CharField(max_length=255, verbose_name="Айыл")

    def __str__(self):
        return f"{self.id_okmot} | {self.name_village}"
