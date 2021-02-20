from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.


def cart(request):
    """ This view returns the cart """
    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add quantity of the menu item to the cart """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    slot = request.session.get('slot', {})
    cart = request.session.get('cart', {})

    if slot == {}:
        messages.error(request, "You need to book a timeslot first!")
        return redirect('timeslot')
    else:
        if item_id in list(cart.keys()):
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

        request.session['cart'] = cart
        print(request.session['slot']) 
        print(request.session['cart'])

        return redirect(redirect_url)