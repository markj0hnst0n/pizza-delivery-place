from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('<int:item_id>/', views.item_detail, name='item_detail'),
    path('add/', views.add_menu_item, name='add_menu_item'),
    path('edit/<int:item_id>/', views.edit_menu_item, name='edit_menu_item'),
    path('delete/<int:item_id>/', views.delete_menu_item,
         name='delete_menu_item'),
]
