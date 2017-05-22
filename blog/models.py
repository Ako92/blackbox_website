from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
import uuid
from geoposition.fields import GeopositionField
# from django.contrib.gis.db import models
# from django.core.files.storage import FileSystemStorage
# from django.contrib.sites.models import Site
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from datetime import datetime
# from django.urls import reverse
# Create your models here.


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'data/users/{0}/{1}'.format(instance.user.username, filename)

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format:"
                                                               " '+999999999'. ""Up to 15 digits allowed.")


class Video(models.Model):
    co_name = models.OneToOneField(to='Customer', null=True)
    project_name = models.CharField(max_length=20)
    video_source = models.FileField(upload_to=user_directory_path, blank=True)
    short_description = models.TextField(max_length=100)
    long_description = models.TextField(max_length=500)
    date_created = models.DateField(blank=True)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):                 # __unicode__ on Python 2
        return self.project_name


class Picture(models.Model):
    co_name = models.OneToOneField('Customer', null=True)
    pic_source = models.ImageField(upload_to=user_directory_path)
    project_name = models.CharField(max_length=20)
    short_description = models.TextField(max_length=100)
    long_description = models.TextField(max_length=500)
    date_created = models.DateField(blank=True)
    date_added = models.DateField(auto_now_add=True)

    def admin_thumbnail(self):
        return u'<img src="%s" />' % self.picture.url

    admin_thumbnail.short_description = 'Thumbnail'
    admin_thumbnail.allow_tags = True

    def __str__(self):              # __unicode__ on Python 2
        return self.project_name


class Profile(models.Model):
    personal_photo = models.ImageField(upload_to=user_directory_path, default='data/profile_default.png')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True)  # validators should be a list
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    linked_in = models.EmailField(blank=True)
    email = models.EmailField(blank=True)
    videos = models.ManyToManyField(Video, null=True, blank=True)
    pictures = models.ManyToManyField(Picture, null=True, blank=True)


class CompanyInfoManager(models.Manager):
    def get_queryset(self):
        return super(CompanyInfoManager, self).get_queryset().filter(co_name='Cixis')


class CompanyInfo(models.Model):
    co_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to=user_directory_path, blank=True)
    short_description = models.TextField(max_length=200, help_text='Max length 200')
    address1 = models.CharField(max_length=150)
    address2 = models.CharField(max_length=150)
    position = GeopositionField(max_length=100, blank=True)
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True)  # validators should be a list
    # social_account = models.ManyToManyField('SocialAccount', blank=True)
    email = models.EmailField()
    objects = models.Manager()
    objects.model = CompanyInfoManager()
    blackBox_object = CompanyInfoManager()
    user = models.ForeignKey(User, blank=True)

    class Meta:
        verbose_name_plural = 'Company information'

    def __str__(self):              # __unicode__ on Python 2
        return self.co_name


class Customer(models.Model):
    customer_id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4,
                                   help_text='Customer Id unique in whole application')
    company_name = models.CharField(max_length=100)
    representative = models.ForeignKey('Profile', on_delete=models.SET_NULL, null=True, blank=True)
    logo = models.ImageField(upload_to=user_directory_path, blank=True)
    address1 = models.CharField(max_length=100, help_text='Address Field 1', blank=True)
    address2 = models.CharField(max_length=100, help_text='Address Field 2', blank=True)
    phone_number = models.CharField(max_length=15, validators=[phone_regex], blank=True)  # validators should be a list
    email = models.EmailField(blank=True)
    videos = models.ManyToManyField(Video, blank=True)
    pictures = models.ManyToManyField(Picture, blank=True)
    user = models.ForeignKey(User, blank=True)

    def __str__(self):
        return '%s, %s' % (self.company_name, self.representative)


class SocialAccount(models.Model):
    user = models.ForeignKey(User, null=True)
    name = models.CharField(max_length=20)
    link = models.URLField()
    logo = models.ImageField(upload_to=user_directory_path)
    co_info = models.ForeignKey(CompanyInfo, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):              # __unicode__ on Python 2
        return self.name
