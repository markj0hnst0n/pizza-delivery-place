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
    """ Adds the requested amount of available slots"""
    """to all current timeslots on the site """

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
            messages.error(
                request, 'No timeslots in database.  Please create a timeslot')
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
            form.save()
            messages.success(request, 'Successfully added Timeslot!')
            return redirect(reverse('timeslot'))
        else:
            messages.error(
                request,
                'Failed to add menu item. Please ensure the form is valid.')
    else:
        form = TimeslotForm()

    template = 'timeslot/create_timeslot.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_timeslot(request, s_id):
    """ Edit a timeslot """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    slot = get_object_or_404(Timeslot, pk=s_id)
    if request.method == 'POST':
        form = TimeslotForm(request.POST, request.FILES, instance=slot)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated timeslot!')
            return redirect(reverse('timeslot'))
        else:
            messages.error(
                request,
                'Failed to update item. Please ensure the form is valid.')
    else:
        form = TimeslotForm(instance=slot)
        messages.info(request, f'You are editing a timeslot for {slot.day}')

    template = 'timeslot/edit_timeslot.html'
    context = {
        'form': form,
        'slot': slot,
    }

    return render(request, template, context)


@login_required
def delete_timeslot(request, s_id):
    """ Delete a day """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    slot = get_object_or_404(Timeslot, pk=s_id)
    slot.delete()
    messages.success(request, 'Timeslot deleted!')
    return redirect(reverse('timeslot'))


@login_required
def add_day(request):
    """ Create a new delivery day on the site """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can use this page.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        day = request.POST.get("day")
        db_day = Day.objects.create(name=day)
        db_day.save()
        return redirect('timeslot')

    return render(request, 'timeslot/add_day.html')


@login_required
def edit_day(request, d_id):
    """ Edit day """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    day = get_object_or_404(Day, pk=d_id)

    if request.method == 'POST':
        day.name = request.POST.get("day")
        day.save()
        messages.success(request, 'Successfully edited day!')
        return redirect('timeslot')

    else:
        messages.info(request, f'You are editing {day.name}')

    template = 'timeslot/edit_day.html'
    context = {
        'day': day,
    }

    return render(request, template, context)


@login_required
def delete_day(request, d_id):
    """ Delete a day """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    day = get_object_or_404(Day, pk=d_id)
    day.delete()
    messages.success(request, 'Day deleted!')
    return redirect(reverse('timeslot'))
