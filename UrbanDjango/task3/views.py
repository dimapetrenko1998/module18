from django.shortcuts import render


def index(request):
    return render(request, 'third_task/index.html')


def shop(request):
    items = {
        'item1': 'Игровая приставка',
        'item2': 'Компьютерные игры',
        'item3': 'Аксессуары для игр',
    }
    return render(request, 'third_task/shop.html', {'items': items})


def cart(request):
    return render(request, 'third_task/cart.html')
