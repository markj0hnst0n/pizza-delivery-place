from django.shortcuts import render
from .models import Timeslot, Time, Day

# Create your views here.
def timeslot(request):    
    """ A view to show all available timeslots """

    slots = Timeslot.objects.all()
    days = Day.objects.all()

    context = {
        'slots': slots,
        'days': days,
    }
    return render(request, 'timeslot/timeslot.html', context)