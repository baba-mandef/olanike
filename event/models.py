from django.db import models


class Event(models.Model):
    """
    Event model
    """
    title = models.CharField(max_length=255)
    description = models.CharField()
    banner = models.ImageField(upload_to='static/img/event')
    start_at = models.DateTimeField()
    finish_at = models.DateTimeField()

    def __str__(self):
        return self.title
