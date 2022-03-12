from django.db import models
from shop import models as md

# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(md.Seller, on_delete=models.CASCADE)
    message = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now=True)