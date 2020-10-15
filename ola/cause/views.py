from django.shortcuts import render


def cause(request):
    return render(request, 'causes.html')
