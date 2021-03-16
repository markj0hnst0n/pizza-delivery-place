from django.contrib import admin
from .models import Day, Timeslot

# Register your models here.




class SlotInline(admin.TabularInline):
    model = Timeslot
    
    

class TimeslotAdmin(admin.ModelAdmin):
    inlines = [
        SlotInline,
    ]
    ordering = ('id',)

class TimeAdmin(admin.ModelAdmin):
    ordering = ('id',)

admin.site.register(Day, TimeslotAdmin)
admin.site.register(Timeslot)