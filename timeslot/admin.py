from django.contrib import admin
from .models import Day, Time, Timeslot

# Register your models here.

admin.site.register(Day)
admin.site.register(Time)
admin.site.register(Timeslot)