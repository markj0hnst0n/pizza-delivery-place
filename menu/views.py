from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import MenuItem, Category

# Create your views here.


def menu(request):    
    """ A view to show all menu items, including sorting and search queries """

    menu = MenuItem.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            menu = menu.filter(queries)
    if 'category' in request.GET:
        categories = request.GET['category'].split(',')
        menu = menu.filter(category__name__in=categories)
        categories = Category.objects.filter(name__in=categories)

    context = {
        'menu': menu,
        'search_term': query,
        'current_categories': categories,
    }
    return render(request, 'menu/menu.html', context)


def item_detail(request, item_id):    
    """ A view to show a specific menu item """

    item = get_object_or_404(MenuItem, pk=item_id)
    
    context = {
        'item': item,
    }
    return render(request, 'menu/item_detail.html', context)
