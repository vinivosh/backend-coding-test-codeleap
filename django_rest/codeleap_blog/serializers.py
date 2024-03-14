from rest_framework import serializers

from codeleap_blog.models import *


class BlogpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogpost
        fields = '__all__'

class BlogpostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogpost
        fields = ['username', 'title', 'content']
