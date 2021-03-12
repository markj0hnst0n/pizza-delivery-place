from django.urls import path
from . import views

urlpatterns = [
    path('', views.timeslot, name='timeslot'),
    path('book/<s_id>/', views.book_a_slot, name='book_a_slot'),
    path('timeslot_refresh/', views.timeslot_refresh, name='timeslot_refresh'),
]