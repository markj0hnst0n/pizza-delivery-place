from django.shortcuts import render, get_object_or_404
from .models import MenuItem

# Create your views here.


def menu(request):    
    """ A view to show all menu items, including sorting and search queries """

    menu = MenuItem.objects.all()
    
    context = {
        'menu': menu,
    }
    return render(request, 'menu/menu.html', context)


def item_detail(request, item_id):    
    """ A view to show a specific menu item """

    item = get_object_or_404(MenuItem, pk=item_id)
    
    context = {
        'item': item,
    }
    return render(request, 'menu/item_detail.html', context)
