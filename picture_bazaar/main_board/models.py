from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class Picture(models.Model):
    title   = models.CharField(max_length=63)
    author  = models.ForeignKey(User, on_delete=models.CASCADE)
    date    = models.DateTimeField(default=now)
    width   = models.IntegerField(auto_created=True)
    height  = models.IntegerField(auto_created=True)
    image   = models.ImageField(width_field='width', height_field='height', upload_to='images')
    tags    = models.CharField(max_length=100)
    favorites = models.ManyToManyField(User, related_name='favorites', blank=True)

    def __str__(self):
        return self.title
