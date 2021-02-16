from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('<item_id>/', views.item_detail, name='item_detail'),
]