from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.


class Customer(models.Model):
    company_name = models.CharField(max_length=100)
    representative = models.TextField()
    logo = models.ImageField()
    address1 = models.CharField(max_length=100, help_text='Address Field 1')
    address2 = models.CharField(max_length=100, help_text='Address Field 2')
    tell = models.IntegerField()
    email = models.EmailField()
    # video = models.ForeignKey
    # picture = models.ForeignKey


class Videos(models.Model):
    video_source = models.FileField()
    short_description = models.TextField(max_length=100)
    long_description = models.TextField(max_length=500)
    date_created = models.DateField(date)


class Pictures(models.Model):
    pic_source = models.ImageField()
    short_description = models.TextField(max_length=100)
    long_description = models.TextField(max_length=500)
    date_created = models.DateField(date)

class CompanyInfo(models.Model):
    co_name = models.CharField(max_length=100)
    logo = models.ImageField
    short_description = models.TextField(max_length=200, help_text='max_length = 200')
    our_videos = models.ForeignKey(to=Videos)
    our_pictures = models.ForeignKey(Pictures)
    address1 = models.TextField(max_length=100)
    address2 = models.TextField(max_length=100)
    tell = models.IntegerField()
    instagram = models.URLField(max_length=20)
    email = models.EmailField()
    facebook = models.URLField


class UserExpanded(models.Model):
    user = models.OneToOneField(User)
