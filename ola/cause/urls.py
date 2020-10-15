from django.urls import path
from ola.cause.views import cause
urlpatterns = [
    path('', cause, name='cause')
]
