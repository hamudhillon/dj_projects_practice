from turtle import title
from django.db import models

# Create your models here.

class blogPost(models.Model):
    title=models.CharField(max_length=255)
    post_by=models.CharField(max_length=255)
    desc=models.CharField(max_length=1000)
    image=models.ImageField(upload_to='blog',null=True)