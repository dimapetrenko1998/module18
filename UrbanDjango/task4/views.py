from django.shortcuts import render
from django.views import View


def home(request):
    return render(request, 'fourth_task/index.html')


def shop(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'The Witcher 3']
    return render(request, 'fourth_task/shop.html', {'games': games})


def cart(request):
    return render(request, 'fourth_task/cart.html')
