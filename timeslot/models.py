from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Day(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class Timeslot(models.Model):
    helptext = "Please use the following format: <em>XX:XX</em>"
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
                                  validators=[MinValueValidator(0),
                                              MaxValueValidator(10)])
