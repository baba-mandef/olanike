from django.urls import path
from ola.event.views import event, details

urlpatterns = [
    path('', event, name='event'),
    path('event/<int:id>/', details, name='event_details')
]