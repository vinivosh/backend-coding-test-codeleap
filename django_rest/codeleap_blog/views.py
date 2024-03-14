# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from rest_framework import status

from codeleap_blog.models import *
from codeleap_blog.serializers import *



# * ############################################################################
# * Class Based Views for basic CRUD operations
# * ############################################################################

class BlogpostAPIView(viewsets.ViewSet):
    # Returns a list with all the names of all codesets in the database
    def read(self, request, pk:int):
        try:
            blogpost = Blogpost.objects.get(pk=pk)
            blogpost_serialized = BlogpostSerializer(blogpost)
            return JsonResponse(blogpost_serialized.data, safe=False, status=status.HTTP_200_OK)
        except Exception as exc:
            return JsonResponse({'message': f'Error! Exception ocurred ({exc.__class__.__name__}): {exc}'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
