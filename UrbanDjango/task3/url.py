from django.urls import path
from ..task3 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
]