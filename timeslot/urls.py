from django.urls import path
from . import views

urlpatterns = [
    path('', views.timeslot, name='timeslot'),
    path('book/<s_id>/', views.book_a_slot, name='book_a_slot'),
    path('timeslot_refresh/', views.timeslot_refresh, name='timeslot_refresh'),
    path('create_timeslot/', views.create_timeslot, name='create_timeslot'),
    path('add_day/', views.add_day, name='add_day'), 
    path('edit_day/<d_id>', views.edit_day, name='edit_day'),
    path('delete_day/<d_id>', views.delete_day, name='delete_day'),
]