from ctypes import addressof
from os import name
from django.db import models

# Create your models here.

class Hospitals(models.Model):
    name = models.CharField(max_length=23)
    address = models.CharField(max_length=23)

    def __str__(self) -> str:
        return self.name

class Continent(models.Model):
    name = models.CharField(max_length=23)

    def __str__(self) -> str:
        return self.name

