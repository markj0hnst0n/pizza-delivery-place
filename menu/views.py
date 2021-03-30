from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import MenuItemForm

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
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('menu'))

            queries = Q(
                name__icontains=query
                ) | Q(
                    description__icontains=query
                    )
            menu = menu.filter(queries)
            if not menu:
                messages.info(request,
                              "Your search returned no results")
                return redirect(reverse('menu'))

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


@login_required
def add_menu_item(request):
    """ Add an item to the menu """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES)
        if form.is_valid():
            menu_item = form.save()
            messages.success(request, 'Successfully added Menu Item!')
            return redirect(reverse('item_detail', args=[menu_item.id]))
        else:
            messages.error(request,
                           'Failed to add menu item. '
                           'Please ensure the form is valid.')
    else:
        form = MenuItemForm()

    template = 'menu/add_menu_item.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_menu_item(request, item_id):
    """ Edit an item on the menu """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    item = get_object_or_404(MenuItem, pk=item_id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated item!')
            return redirect(reverse('item_detail', args=[item.id]))
        else:
            messages.error(request,
                           'Failed to update item. '
                           'Please ensure the form is valid.')
    else:
        form = MenuItemForm(instance=item)
        messages.info(request, f'You are editing {item.name}')

    template = 'menu/edit_menu_item.html'
    context = {
        'form': form,
        'item': item,
    }

    return render(request, template, context)


@login_required
def delete_menu_item(request, item_id):
    """ Delete a item from the menu """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    item = get_object_or_404(MenuItem, pk=item_id)
    item.delete()
    messages.success(request, 'Menu item deleted!')
    return redirect('menu')
