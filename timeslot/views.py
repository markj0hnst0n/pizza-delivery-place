from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import TimeslotForm

from .models import Timeslot, Day


def timeslot(request):    
    """ A view to show all available timeslots """

    slots = Timeslot.objects.all().order_by('start_time')
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

    if request.method == 'POST':
        all_slots = Timeslot.objects.all()

        if all_slots:
            slots_to_add = int(request.POST.get("slot_num"))
            for slot in all_slots:
                slot.available_slots = 0
                slot.available_slots += slots_to_add
                slot.save()
        else:
            messages.error(request, 'No timeslots in database.  Please create a timeslot')
            return redirect('home')

    
    return redirect('timeslot')

@login_required
def create_timeslot(request):
    """ Create a timeslot on the site """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can use this page.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TimeslotForm(request.POST, request.FILES)
        if form.is_valid():
            menu_item = form.save()
            messages.success(request, 'Successfully added Timelsot!')
            return redirect(reverse('timeslot'))
        else:
            messages.error(request,
                           'Failed to add menu item. Please ensure the form is valid.')
    else:
        form = TimeslotForm()
    
    template = 'timeslot/create_timeslot.html'
    context = {
        'form': form,
    }

    return render(request, template, context)

# @login_required
# def create_day(request):
#     """ Create a new delivery day on the site """

#     if not request.user.is_superuser:
#         messages.error(request, 'Sorry, only store owners can use this page.')
#         return redirect(reverse('home'))
