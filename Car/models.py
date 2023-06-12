from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Workshop(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    oldtimer_friendly = models.BooleanField()

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    manuf_name = models.CharField(max_length=255)
    webpage = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    owner = models.CharField(max_length=255)

    def __str__(self):
        return self.manuf_name


class ManufWorkshop(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)

    def __str__(self):
        return self.manufacturer.manuf_name + " " + self.workshop.name


class Car(models.Model):
    type = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    max_speed = models.IntegerField()
    colour = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class Fix(models.Model):
    code = models.CharField(max_length=255)
    date = models.DateField()
    desc = models.TextField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField()
    fix_car = models.ForeignKey(Car, on_delete=models.CASCADE)
    fix_workshop = models.ForeignKey(Workshop, on_delete=models.CASCADE)

    def __str__(self):
        return self.code
