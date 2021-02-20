
from django.conf import settings
from django.shortcuts import get_object_or_404
from menu.models import MenuItem

def cart_contents(request):

    cart_items = []
    total = 0
    item_count = 0
    delivery = 2
    grand_total = 0
    cart = request.session.get('cart', {})

    
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

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context