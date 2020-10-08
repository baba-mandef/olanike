from django.urls import path
from event.views import event

urlpatterns = [
    path('', event, name='event')
]
