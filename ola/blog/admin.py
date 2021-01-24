from django.contrib import admin
from ola.blog.models import (Category, Post, Comment, Author, Counter)

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
# admin.site.register(Comment)
admin.site.register(Author)
# admin.site.register(Counter)
