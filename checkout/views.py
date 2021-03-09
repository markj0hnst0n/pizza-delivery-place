from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings

from menu.models import MenuItem
from timeslot.models import Timeslot
from profiles.models import UserProfile
from profiles.forms import UserProfileForm
from .models import Order, OrderLineItem
from .forms import OrderForm
from cart.contexts import cart_contents

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    slot = request.session.get('slot', {})
    if 'slot' in request.session:
        s_id = list(slot.keys())[list(slot.values()).index(True)]
        db_slot = get_object_or_404(Timeslot, pk=s_id)
        if db_slot.available_slots < 1:        
            messages.error(request, "All requested slots now booked.  Please try another slot")
            del request.session['slot']
            return redirect('timeslot')
    else:
        messages.error(request, "You need to book a timeslot!")
        return redirect('timeslot')
    
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        slot = request.session.get('slot', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'county': request.POST['county'],
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart),
            order.save()
            for item_id, quantity in cart.items():
                try:
                    item = MenuItem.objects.get(id=item_id)

                    order_line_item = OrderLineItem(
                        order=order,
                        item=item,
                        quantity=quantity,
                    )
                    order_line_item.save()

                except MenuItem.DoesNotExist:
                    messages.error(request, (
                        "One of the items in your cart wasn't found in our database. "
                        "Please call us for assistance!")
                    )
                    order.delete()
                    return redirect(reverse('cart'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
        

    else:
        slot = request.session.get('slot', {})
        cart = request.session.get('cart', {})

        if not slot:
            messages.error(request, "You have not booked a slot yet")
            return redirect(reverse('timeslot'))

        if not cart:
            messages.error(request, "You have no items in your cart")
            return redirect(reverse('menu'))

        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is not set')

    
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """

    slot = request.session.get('slot', {})
    if 'slot' in request.session:
        s_id = list(slot.keys())[list(slot.values()).index(True)]
        db_slot = get_object_or_404(Timeslot, pk=s_id)
        db_slot.available_slots -= 1
        db_slot.save()
        del request.session['slot']
    else:
        messages.error(request, "You need to book a timeslot first!")
        return redirect('timeslot')
    
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)

        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                'default_full_name': order.full_name,
                'default_street_address1': order.street_address1,
                'default_street_address2': order.street_address2,
                'default_town_or_city': order.town_or_city,
                'default_county': order.county,
                'default_postcode': order.postcode,
                'default_phone_number': order.phone_number,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
    
    
    if 'cart' in request.session:
        del request.session['cart']
        

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
