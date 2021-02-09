from django.shortcuts import render
from .models import MenuItem

# Create your views here.


def menu(request):    
    """ A view to show all menu items, including sorting and search queries """

    menu = MenuItem.objects.all()
    
    context = {
        'menu': menu,
    }
    return render(request, 'menu/menu.html', context)
