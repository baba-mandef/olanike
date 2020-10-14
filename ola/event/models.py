from django.db import models


class Event(models.Model):
    """
    Event model
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    banner = models.ImageField(upload_to='events_pics')
    start_at = models.DateTimeField()
    finish_at = models.DateTimeField()
    adress = models.CharField(max_length=255)

    def __str__(self):
        return self.title
