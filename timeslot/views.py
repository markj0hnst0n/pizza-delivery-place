from django.shortcuts import render, redirect
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

    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    cart[F"slot_{s_id}"] = True
    request.session['cart'] = cart
    print(request.session['cart'])

    return redirect('menu')