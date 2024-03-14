"""
URL configuration for codeleap_blog app.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

from codeleap_blog import views

urlpatterns = [
    # (GET) Retrieve a single Blogpost
    # (PATCH) Update a single Blogpost
    # (DELETE) Delete a single Blogpost
    path(r'api/blogpost/<pk>', views.BlogpostAPIView.as_view({'get': 'read', 'patch': 'update', 'delete': 'delete'})),\

    # (GET) Retrieve all Blogposts
    # (POST) Create a new Blogpost
    path(r'api/blogpost', views.BlogpostAPIView.as_view({'get': 'list', 'post': 'create'})),
]
