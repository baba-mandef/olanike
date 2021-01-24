from django.shortcuts import render
from ola.cause.models import Cause


def causes(request):
    causes = Cause.objects.filter(is_active=True)
    context = {'causes':causes}
    return render(request, 'causes.html', context)

def cause_details(request, slug):
    cause = Cause.objects.get(slug=slug)
    context = {'cause':cause}
    return render(request, 'cause-details.html', context)
