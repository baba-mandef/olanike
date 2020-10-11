from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from ola.blog.models import Post, Category, Comment, Author
from ola.blog.forms import CommentForm


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
    # post = Post.objects.get(pk=id)
    post = get_object_or_404(Post, post_id=id)
    last = Post.objects.order_by('created_at')[:5]
    cat = Category.objects.all()
    comments = Comment.objects.filter(post=id)
    form = CommentForm
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    author = Author.objects.get(pk=post.author.pk)
    return render(request, 'details.html', {'post': post, 'last': last, 'cat': cat, 'comments': comments, 'form': form, 'author': author})
