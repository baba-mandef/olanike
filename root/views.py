from django.shortcuts import render
from blog.models import Post


def home(request):
    """
    Home view function
    """
    latest = Post.objects.order_by('created_at')[:2]
    return render(request, 'home.html', {'latest' : latest,})
