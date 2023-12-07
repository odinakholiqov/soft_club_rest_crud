from django.db import models
from django.contrib.auth.models import User 


class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=255)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    