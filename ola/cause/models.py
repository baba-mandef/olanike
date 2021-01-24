from django.db import models
from tinymce.models import HTMLField


class Cause(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.SlugField(max_length=255)
    title = models.CharField(max_length=255)
    banner = models.ImageField(upload_to='cause_pics')
    goal = models.IntegerField()
    level = models.IntegerField()
    description = HTMLField()
    don_number = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Don(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    donation = models.IntegerField()
    cause = models.ForeignKey(Cause, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname
