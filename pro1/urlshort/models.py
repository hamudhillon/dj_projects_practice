from django.db import models

# Create your models here.

class urls(models.Model):
    long_url=models.CharField(max_length=255)
    short_url_id=models.CharField(max_length=255)