from django.shortcuts import render
from ola.blog.models import Post
from ola.cause.models import Cause
from ola.event.models import Event


def home(request):
    """
    Home view function
    """
    last_cause = Cause.objects.filter(is_active=True).order_by('created_at')[:2]
    latest = Post.objects.filter(published=True).order_by('created_at')[:2]
    last_event = Event.objects.filter(is_active=True).order_by('start_at')[:4]
    context = {'latest': latest, 'last_event': last_event, 'last_cause':last_cause}
    return render(request, 'home.html', context)
