from django.db import models


class Cause(models.Model):
    id = models.AutoField(primay_key=True)
    title = models.CharField(max_length=255)
    banner = models.ImageField(upload_to='cause_pics')
    goal = models.IntegerField()
    level = models.IntegerField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Category(models.Model):
    id = models.AutoField(primay_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Don(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField()
    email = models.EmailField()
    donation = models.IntegerField()
    quote = models.TextField()

    def __str__(self):
        return self.fullname
