from django.contrib import admin
from django.urls import path, include
from root.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('blog/', include('ola.blog.urls')),  # add blog path
    path('events/', include('ola.event.urls')),  # add event path
]
