from django.urls import path
from blog.views import posts

urlpatterns = [

    path('', posts, name='posts'),

]
