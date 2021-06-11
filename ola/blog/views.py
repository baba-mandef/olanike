from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from ola.blog.models import (Post, Category, Comment, Author, Counter)
from ola.blog.forms import CommentForm
from ola.utils.ip import get_ip


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


def details(request, slug):
    # post = Post.objects.get(pk=id)
    post = get_object_or_404(Post, slug=slug)
    last = Post.objects.order_by('created_at')[:5]
    cat = Category.objects.all()
    ip = get_ip(request)
    check_ip = Counter.objects.filter(ipAdress=ip, post=post)
    comments = Comment.objects.filter(post__slug=slug)
    form = CommentForm
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    author = Author.objects.get(pk=post.author.pk)
    if check_ip:
        post.view = post.view
        post.save()
    elif not check_ip and post.published:
        new_ip = Counter(post=post, ipAdress=ip)
        new_ip.save()
        post.view = post.view+1
        post.save()
    return render(request, 'details.html', {'post': post, 'last': last, 'cat': cat, 'comments': comments, 'form': form, 'author': author})
