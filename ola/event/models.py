from django.db import models
from tinymce.models import HTMLField


class Event(models.Model):
    """
    Event model
    """
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = HTMLField()
    banner = models.ImageField(upload_to='events_pics')
    start_at = models.DateTimeField()
    finish_at = models.DateTimeField()
    adress = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
