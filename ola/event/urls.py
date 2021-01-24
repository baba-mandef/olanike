from django.urls import path
from ola.event.views import event, details

urlpatterns = [
    path('', event, name='event'),
    path('event/<str:slug>/', details, name='event_details')
]
