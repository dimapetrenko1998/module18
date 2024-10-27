from django.shortcuts import render
from django.views import View


# Create your views here.

def home(request):
    return render(request, 'second_task/home.html')


def functional_view(request):
    return render(request, 'second_task/func_template.html')


class ClassBasedView(View):
    def get(self, request):
        return render(request, 'second_task/class_template.html')




