from django.db import models

# Create your models here

class Day(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Time(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Timeslot(models.Model):    
    day = models.ForeignKey('Day', null=True, blank=True, on_delete=models.SET_NULL)
    time = models.ForeignKey('Time', null=True, blank=True, on_delete=models.SET_NULL)
    available_slots = models.IntegerField(null=True)
