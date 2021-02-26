from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    cart = request.session.get('cart', {})
    slot = request.session.get('slot', {})
    
    if not slot:
        messages.error(request, "You have not booked a slot yet")
        return redirect(reverse('timeslot'))

    if not cart:
        messages.error(request, "You have no items in your cart")
        return redirect(reverse('menu'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form
    }

    return render(request, template, context)