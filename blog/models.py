from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class blog_model(models.Model):
    blog_name=models.CharField(max_length=200)
    blog_content=models.TextField()
    date_posted=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.blog_name

