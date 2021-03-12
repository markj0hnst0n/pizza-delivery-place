from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Timeslot, Time, Day


def timeslot(request):    
    """ A view to show all available timeslots """

    slots = Timeslot.objects.all()
    days = Day.objects.all()
    total_slot_list = []
    total_slots = 0

    for s in slots:
        total_slot_list.append(s.available_slots)
    
    total_slots = sum(total_slot_list)

    context = {
        'slots': slots,
        'days': days,
        'total_slots': total_slots,
    }
    
    return render(request, 'timeslot/timeslot.html', context)

def book_a_slot(request, s_id):
    """ Reserve a slot from the database and add it to the session """

    slot = request.session.get('slot', {})
    if slot:
        messages.error(request, "You've booked a slot already")
        return redirect('menu')
    else:
        slot[s_id] = True
        request.session['slot'] = slot

        messages.success(request, "Slot booked in!")
        return redirect('menu')


@login_required
def timeslot_refresh(request):
    """ Adds 2 available slots to all current timeslots on the site """
    """ This view assumes all slots are sold out currently """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can use this page.')
        return redirect(reverse('home'))

    all_slots = Timeslot.objects.all()

    for slot in all_slots:
        slot.available_slots = 0
        slot.available_slots += 2
        slot.save()
    
    return redirect('timeslot')
