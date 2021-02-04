from django.shortcuts import render

# Create your views here.


def index(request):
    """ Returned Index/Homepage """
    return render(request, 'home/index.html')