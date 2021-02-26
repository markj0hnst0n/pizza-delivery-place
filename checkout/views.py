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
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IDcERKBTecb2BhiyhQgAxXamUTTNBaO4scYLCIaZnHjbb9fYxJ472qqskVZiaJbp66qqxqr4rVbK4a0J88uGrd700X7IpDUEa',
        'client_secret': 'test_secret'
    }

    return render(request, template, context)