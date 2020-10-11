from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ola.home.urls')),
    path('blog/', include('ola.blog.urls')),  # add blog path
    path('events/', include('ola.event.urls')),  # add event path
]
