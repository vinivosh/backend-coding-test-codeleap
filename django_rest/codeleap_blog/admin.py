from django.contrib import admin

from codeleap_blog.models import *



@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    list_display = ('title', 'username', 'id', 'created_datetime')
    search_fields = ['id', 'username', 'title']

    ordering = ['-created_datetime']
