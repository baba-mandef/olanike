from django.shortcuts import render


def home(request):
    """
    Home view function
    """

    return render(request, 'home.html')
