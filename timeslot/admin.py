from django.contrib import admin
from .models import Day, Time, Timeslot

# Register your models here.




class SlotInline(admin.TabularInline):
    model = Timeslot

class TimeslotAdmin(admin.ModelAdmin):
    inlines = [
        SlotInline,
    ]


admin.site.register(Day, TimeslotAdmin)
