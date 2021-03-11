from django.shortcuts import render

# Create your views here.


def index(request):
    """ Returns Index/Homepage """
    return render(request, 'home/index.html')

def about(request):
    """ Shows about page for the business """
    return render(request, 'home/about.html')