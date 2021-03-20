from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from checkout.models import Order
from .models import UserProfile
from .forms import UserProfileForm


@login_required
def profile(request):
    """ Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated!')
        else:
            messages.error(request, 'Update failed.  Form is not valid.')
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all().order_by('-date')

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def admin(request):
    """ Display's admin page for owners/managers. """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can use this page.')
        return redirect(reverse('home'))

    orders = Order.objects.all()
    query = None

    if request.GET:
        if 'order_q' in request.GET:
            query = request.GET['order_q']
            if not query:
                messages.error(request,
                               "You didn't enter any search criteria!")
                return redirect(reverse('admin'))

            queries = Q(
                order_number__icontains=query) | Q(full_name__icontains=query)
            orders = orders.filter(queries)

    template = 'profiles/admin.html'
    context = {
        'orders': orders
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
