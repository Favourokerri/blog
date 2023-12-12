from django.db import models
from ckeditor.fields import RichTextField
from Profile.models import Profile
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    """models for category field"""
    category = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.category


class BlogPost(models.Model):
    image = models.ImageField(upload_to='post_images/', null=True, blank=True)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    content = RichTextField(default="Post content")
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=200, default="user")
    email = models.CharField(max_length=300, blank=True, null=True)
    comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment[:50]

class NewsLetter(models.Model):
    """ models for newsletter"""
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.email