from django.conf import settings
from django.shortcuts import get_object_or_404
from menu.models import MenuItem
from timeslot.models import Timeslot


def cart_contents(request):

    cart_items = []
    booked_slot = ""
    total = 0
    item_count = 0
    delivery = settings.DEFAULT_DELIVERY_CHARGE
    grand_total = 0
    cart = request.session.get('cart', {})
    slot = request.session.get('slot', {})

    for item_id, quantity in cart.items():
        item = get_object_or_404(MenuItem, pk=item_id)
        total += quantity * item.price
        item_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'item': item,
        })

    if cart_items:
        grand_total = delivery + total

    for s_id in slot.keys():
        booked_slot = get_object_or_404(Timeslot, pk=s_id)

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'grand_total': grand_total,
        'booked_slot': booked_slot,
    }

    return context
