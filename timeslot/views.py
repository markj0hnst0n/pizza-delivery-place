from django.shortcuts import render

# Create your views here.
def timeslot(request):    
    """ A view to show all available timeslots """

    slots = Timeslot.objects.all()
    
    context = {
        'slots': slots,
    }
    return render(request, 'timeslot/timeslot.html', context)
