from django.urls import path
from ola.home.views import home

urlpatterns = [
    path('', home, name='home'),
]
