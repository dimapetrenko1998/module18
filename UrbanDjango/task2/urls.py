from django.urls import path
from .views import functional_view, ClassBasedView, home

urlpatterns = [
    path('', home, name='home'),
    path('func/', functional_view, name='functional_view'),
    path('class/', ClassBasedView.as_view(), name='class_view'),
]
