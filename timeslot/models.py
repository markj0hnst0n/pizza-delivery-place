from django.db import models

# Create your models here

class Day(models.Model):
    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Timeslot(models.Model):    
    day = models.ForeignKey('Day', null=True, blank=True, on_delete=models.SET_NULL)
    start_time = models.TimeField('StartTime', null=True, blank=True)
    end_time = models.TimeField('EndTime', null=True, blank=True)
    available_slots = models.PositiveIntegerField(null=True)
