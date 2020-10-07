from django.db import models


class Post(models.Model):
    """
    post model
    create an return new post
    """
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    body = models.TextField()
    banner = models.ImageField(upload_to='static/img/blog')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)  # post category
    created_at = models.DateTimeField(auto_now_add=True,)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    """
    post category model
    create and return new category
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
