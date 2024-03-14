from rest_framework import serializers

from codeleap_blog.models import *


class BlogpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogpost
        fields = '__all__'
