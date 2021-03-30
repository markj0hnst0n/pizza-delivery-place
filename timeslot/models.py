from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Day(models.Model):
    name = models.CharField(max_length=32)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Timeslot(models.Model):
    helptext = "Please use the following format: <em>XX:XX</em>"
    min_val = MinValueValidator(0)
    max_val = MaxValueValidator(10)
    day = models.ForeignKey('Day',
                            null=True,
                            blank=True,
                            on_delete=models.CASCADE)
    start_time = models.TimeField('Start Time',
                                  null=True,
                                  help_text=helptext)
    end_time = models.TimeField('End Time',
                                null=True,
                                help_text=helptext)
    available_slots = models.PositiveSmallIntegerField(null=True,
                                                       validators=[min_val,
                                                                   max_val])
