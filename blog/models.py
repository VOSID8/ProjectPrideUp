from sre_constants import MAX_UNTIL
from django.db import models
from shop.models import Seller
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Seller, on_delete=models.CASCADE)
    text = models.TextField()
    date = models.DateField(auto_now=True, blank=True)
    views = models.PositiveIntegerField(default=0, blank=True)
    slug = models.CharField(max_length=70)
    likes = models.ManyToManyField(User, blank=True)
    image = models.ImageField(upload_to='static/blog/images/upload', null=True)

class Comment(models.Model):
    content = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True, blank=True)
    parent = models.ForeignKey('Comment', on_delete=models.CASCADE)