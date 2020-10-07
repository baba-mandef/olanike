from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post


def posts(request):
    """
    post list view function
    """
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'blog.html', {'posts': posts})
