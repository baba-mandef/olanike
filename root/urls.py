from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ola.home.urls')),
    path('blog/', include('ola.blog.urls')),  # add blog path
    path('events/', include('ola.event.urls')),  # add event path
    path('causes/', include('ola.cause.urls')),  # add cause route
    path('tinymce/', include('tinymce.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
