from django.urls import path
from ola.cause.views import (causes, cause_details)
urlpatterns = [
    path('', causes, name='cause'),
    path('cause/<str:slug>', cause_details, name='cause-details')
]
