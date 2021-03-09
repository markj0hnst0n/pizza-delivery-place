from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('<int:item_id>/', views.item_detail, name='item_detail'),
    path('add/', views.add_menu_item, name='add_menu_item'),
]