from django.urls import path
from . import views

urlpatterns = [
    path('', views.timeslot, name='timeslot'),
]
