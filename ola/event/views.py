from django.shortcuts import render
from django.core.paginator import Paginator
from ola.event.models import Event


def event(request):
    events_list = Event.objects.filter(is_active=True).order_by('start_at')
    paginator = Paginator(events_list, 6)
    page = request.GET.get('page')
    events = paginator.get_page(page)

    return render(request, 'event.html', {'events': events})  # ToDO : countdown system


def details(request,slug):
    events = Event.objects.get(slug=slug)
    return render(request, 'event-details.html', {'event': events})
