from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Timeslot, Time, Day


def timeslot(request):    
    """ A view to show all available timeslots """

    slots = Timeslot.objects.all()
    days = Day.objects.all()

    context = {
        'slots': slots,
        'days': days,
    }
    return render(request, 'timeslot/timeslot.html', context)

def book_a_slot(request, s_id):
    """ Reserve a slot and add it to the cart """

    slot = request.session.get('slot', {})
    db_slot = get_object_or_404(Timeslot, pk=s_id)
    if slot:
        messages.error(request, "You've booked a slot already")
        return redirect('menu')
    else:
        slot[s_id] = True
        request.session['slot'] = slot
        db_slot.available_slots -= 1
        db_slot.save()

        messages.success(request, "Slot booked in!")
        return redirect('menu')