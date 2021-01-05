from django.urls import path
from ola.blog.views import posts, categories, details

urlpatterns = [

    path('', posts, name='posts'),
    path('posts/<str:cate>/', categories, name='category'),
    path('post/<str:slug>/', details, name='details'),

]
