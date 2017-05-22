from rest_framework import serializers
from blog.models import CompanyInfo, Customer, Picture, Video, Profile


class ProfileSerializer(serializers.Serializer):
    personal_photo = serializers.ImageField(allow_null=True)
    phone_number = serializers.IntegerField(allow_null=True,required=False)
    bio = serializers.CharField(max_length=500)
    birth_date = serializers.DateField(allow_null=True)
    email = serializers.EmailField()
    linked_in = serializers.URLField(allow_null=True)


class VideoSerializer(serializers.Serializer):
    project_name = serializers.CharField(max_length=20)
    short_description = serializers.CharField(max_length=200)
    long_description = serializers.CharField(max_length=500)
    date_created = serializers.DateField()
    video_path = serializers.FileField(allow_empty_file=True)

