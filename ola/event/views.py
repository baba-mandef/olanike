from django.shortcuts import render
from django.core.paginator import Paginator
from ola.event.models import Event


def event(request):
    events_list = Event.objects.all()
    paginator = Paginator(events_list, 6)
    page = request.GET.get('page')
    events = paginator.get_page(page)

    return render(request, 'event.html', {'events': events})  # ToDO : countdown system


def details(request,id):
    event = Event.objects.get(pk=id)
    return render(request, 'event-details.html', {'event': event})
