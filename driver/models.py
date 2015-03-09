from django.db import models

class Trip(models.Model):
    name = models.CharField(max_length=100)
    distance = models.DecimalField(max_digits=50, decimal_places=2, null=True)
    duration = models.TimeField(null=True)
    mood = models.CharField(max_length=50, null=True)

class Service(models.Model):
    description = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=50, decimal_places=2, null=True)
    date = models.DateField(null=True)

