from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='post_images/', null=True, blank=True, default='default/default.jpeg')

    def __str__(self):
        return self.user.username

class Contact(models.Model):
    email = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    facebook_link = models.URLField(blank=True, null=True, help_text='can be left blank')
    instagram_link = models.URLField(blank=True, null=True, help_text='can be left blank')
    twitter_link = models.URLField(blank=True, null=True, help_text='can be left blank')
    whatsapp_link = models.URLField(blank=True, null=True, help_text='can be left blank')

class About(models.Model):
    about = models.TextField()

    def __str__(self):
        return self.about[:20]

class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.CharField(max_length=400)