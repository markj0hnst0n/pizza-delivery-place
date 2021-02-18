from django.shortcuts import render

# Create your views here.


def cart(request):
    """ Returned Index/Homepage """
    return render(request, 'cart/cart.html')
