from django.shortcuts import render
from ola.blog.models import Post
from ola.event.models import Event


def home(request):
    """
    Home view function
    """
    latest = Post.objects.order_by('created_at')[:2]
    last_event = Event.objects.order_by('start_at')[:4]
    return render(request, 'home.html', {'latest': latest, 'last_event': last_event})
