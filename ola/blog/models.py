from django.db import models


class Post(models.Model):
    """
    post model
    create an return new post
    """
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    banner = models.ImageField(upload_to='blog_pics')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)  # post category
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    view = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    body = models.TextField()
    author_name = models.CharField(max_length=20)
    author_pic = models.ImageField(default='static/img/blog/comment/d.png')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author_name


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    bio = models.TextField()
    picture = models.ImageField(upload_to='author_pics')

    def __str__(self):
        return self.name


class Category(models.Model):
    """
    post category model
    create and return new category
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
