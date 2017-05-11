from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import uuid
from geoposition.fields import GeopositionField
from django.core.files.storage import FileSystemStorage
# from django.contrib.sites.models import Site
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from datetime import datetime
# from django.urls import reverse
# Create your models here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'data/user_{0}/{1}'.format(instance.user.id, filename)

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format:"
                                                               " '+999999999'. ""Up to 15 digits allowed.")


class Profile(models.Model):
    personal_photo = models.ImageField(upload_to='uploaded/profile/picture',blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True)  # validators should be a list
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    # videos = models.ForeignKey('Video')
    # picture = models.ForeignKey('Picture')


class Video(models.Model):
    project_name = models.CharField(max_length=20)
    video_path = models.FileField(upload_to='uploaded/customer/videos')
    short_description = models.TextField(max_length=100)
    long_description = models.TextField(max_length=500)
    date_created = models.DateField()

    def __str__(self):              # __unicode__ on Python 2
        return self.project_name


class Picture(models.Model):
    pic_source = models.ImageField(upload_to='uploaded/customer/pics')
    project_name = models.CharField(max_length=20)
    short_description = models.TextField(max_length=100)
    long_description = models.TextField(max_length=500)
    date_created = models.DateField()
    date_added = models.DateField()

    def __str__(self):              # __unicode__ on Python 2
        return self.project_name

class CompanyInfo(models.Model):
    # site = models.OneToOneField(Site)
    co_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='uploaded/website/',blank=True)
    short_description = models.TextField(max_length=200, help_text='Max length 200')
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150)
    position = GeopositionField()
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True)  # validators should be a list
    instagram = models.EmailField(blank=True)
    info_email = models.EmailField()

    class Meta:
        verbose_name_plural = 'Company information'

    def __str__(self):              # __unicode__ on Python 2
        return self.co_name


class Customer(models.Model):
    customer_id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                                   help_text='Customer Id unique in whole application')
    company_name = models.CharField(max_length=100)
    representative = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True, blank=True)
    logo = models.FilePathField()
    address1 = models.CharField(max_length=100, help_text='Address Field 1')
    address2 = models.CharField(max_length=100, help_text='Address Field 2', blank=True)
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True)  # validators should be a list
    email = models.EmailField()
    videos = models.ForeignKey('Video')
    pictures = models.ForeignKey('Picture')

    def __str__(self):
        return '%s, %s' % (self.company_name, self.representative)

