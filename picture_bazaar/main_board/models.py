from django.db import models
from django.contrib.auth.models import User


class Picture(models.Model):
    title = models.CharField(max_length=63)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    width = models.IntegerField(auto_created=True, blank=True)
    height = models.IntegerField(auto_created=True, blank=True)
    image = models.ImageField(width_field='width', height_field='height', upload_to='images')
    tags = models.TextField()