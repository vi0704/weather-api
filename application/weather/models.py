from django.db import models


class State(models.Model):
    state = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now=True, null=True, blank=True)


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    lat = models.DecimalField(decimal_places=5, max_digits=8)
    lng = models.DecimalField(decimal_places=5, max_digits=8)
    created_on = models.DateTimeField(auto_now=True, null=True, blank=True)


class Temperature(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    date = models.DateTimeField()
    temperature = models.TextField()
    created_on = models.DateTimeField(auto_now=True, null=True, blank=True)