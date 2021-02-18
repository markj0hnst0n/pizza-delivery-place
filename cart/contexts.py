def cart_contents(request):

    cart_items = []
    total = 0
    item_count = 0
    delivery = 2
    grand_total = 0

    if cart_items:
        grand_total = delivery + total
        return grand_total

    context = {
        'cart_items': cart_items,
        'total': total,
        'item_count': item_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context
