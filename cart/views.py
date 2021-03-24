from menu.models import MenuItem
from django.contrib import messages
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.shortcuts import get_object_or_404


def cart(request):
    """ This view returns the cart """
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    """ Add quantity of the menu item to the cart """

    item = get_object_or_404(MenuItem, pk=item_id)
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
        messages.success(request, f'Added {item.name} to cart!')
        return redirect(redirect_url)


def adjust_cart(request, item_id):
    """ Adjust quantity of the menu item """

    item = get_object_or_404(MenuItem, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    slot = request.session.get('slot', {})
    cart = request.session.get('cart', {})

    if slot == {}:
        messages.error(request, "You need to book a timeslot first!")
        return redirect('timeslot')
    else:
        if quantity > 0:
            cart[item_id] = quantity
            messages.success(request, f'Updated {item.name}\
                 quantity to {cart[item_id]}')
        else:
            cart.pop[item_id]
            messages.success(request, f'Removed {item.name}\
                 from shopping cart')

        request.session['cart'] = cart
        return redirect(reverse('cart'))


def remove_from_cart(request, item_id):
    """ Remove menu item from bag """

    item = get_object_or_404(MenuItem, pk=item_id)
    slot = request.session.get('slot', {})
    cart = request.session.get('cart', {})

    try:
        if slot == {}:
            messages.error(request, "You need to book a timeslot first!")
            return redirect('timeslot')
        else:
            cart.pop(item_id)
            messages.success(request, f'Removed {item.name}\
                 from shopping cart')

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
