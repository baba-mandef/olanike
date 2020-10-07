from django.urls import path
from blog.views import posts, categories, details

urlpatterns = [

    path('', posts, name='posts'),
    path('posts/<str:cate>/', categories, name='category'),
    path('post/<int:id>/', details, name='details'),

]
