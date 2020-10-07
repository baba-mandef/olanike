from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import Post, Category


def posts(request):
    """
    post list view function
    """
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 4)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    cat = Category.objects.all()
    last = Post.objects.order_by('created_at')[:5]
    return render(request, 'blog.html', {'posts': posts, 'cat': cat, 'last': last})


def categories(request, cate):
    cat_list = Post.objects.filter(category__name=cate)
    paginator = Paginator(cat_list, 5)
    page = request.GET.get('page')
    category = paginator.get_page(page)
    return render(request, 'category.html', {'category': category})


def details(request, id):
    post = Post.objects.get(pk=id)
    last = Post.objects.order_by('created_at')[:5]
    cat = Category.objects.all()
    return render(request, 'details.html', {'post': post, 'last': last, 'cat': cat})
