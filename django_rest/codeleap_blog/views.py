# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from django.http.response import HttpResponse
from django.http.response import JsonResponse
from rest_framework import status

from codeleap_blog.models import *
from codeleap_blog.serializers import *



# * ############################################################################
# * Class Based Views for basic CRUD operations
# * ############################################################################

class BlogpostAPIView(viewsets.ViewSet):
    def read(self, request, pk:int):
        '''Returns a single Blogpost by ID'''

        try:
            blogpost = Blogpost.objects.get(pk=pk)
            blogpost_serialized = BlogpostSerializer(blogpost)
            return JsonResponse(blogpost_serialized.data, safe=False, status=status.HTTP_200_OK)
        except Blogpost.DoesNotExist:
            return JsonResponse({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as exc:
            return JsonResponse({'detail': f'Error! Exception ocurred ({exc.__class__.__name__}): {exc}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def list(self, request):
        '''Returns *ALL* Blogposts'''

        try:
            blogposts = Blogpost.objects.all()
            blogposts_serialized = BlogpostSerializer(blogposts, many=True)

            # Organizing data the exact same way as returned by a GET request to https://dev.codeleap.co.uk/careers/
            body = {
                'count': len(blogposts_serialized.data),
                'next': None,
                'previous': None,
                'results': blogposts_serialized.data,
            }
            return JsonResponse(body, safe=False, status=status.HTTP_200_OK)
        except Exception as exc:
            return JsonResponse({'detail': f'Error! Exception ocurred ({exc.__class__.__name__}): {exc}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def create(self, request):
        '''Creates a new Blogpost'''

        try:
            blogpost_data = JSONParser().parse(request)
            blogpost_serialized = BlogpostCreateSerializer(data=blogpost_data)
            if blogpost_serialized.is_valid():
                blogpost_created:Blogpost = blogpost_serialized.save()
                blogpost_serialized = BlogpostSerializer(blogpost_created)
                return JsonResponse(blogpost_serialized.data, status=status.HTTP_201_CREATED)
            return JsonResponse(blogpost_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as exc:
            return JsonResponse({'detail': f'Error! Exception ocurred ({exc.__class__.__name__}): {exc}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def update(self, request, pk:int):
        '''Updates a single Blogpost by ID'''

        try:
            blogpost = Blogpost.objects.get(pk=pk)
            blogpost_data = JSONParser().parse(request)
            blogpost_serialized = BlogpostUpdateSerializer(blogpost, data=blogpost_data, partial=True)
            if blogpost_serialized.is_valid():
                blogpost_updated:Blogpost = blogpost_serialized.save()
                blogpost_serialized = BlogpostSerializer(blogpost_updated)
                return JsonResponse(blogpost_serialized.data, status=status.HTTP_200_OK)
            return JsonResponse(blogpost_serialized.errors, status=status.HTTP_400_BAD_REQUEST)
        except Blogpost.DoesNotExist:
            return JsonResponse({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as exc:
            return JsonResponse({'detail': f'Error! Exception ocurred ({exc.__class__.__name__}): {exc}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self, request, pk:int):
        '''Deletes a single Blogpost by ID'''

        try:
            blogpost = Blogpost.objects.get(pk=pk)
            blogpost.delete()

            # Returning nothing at all, as is done by sending a valid (DELETE) request to https://dev.codeleap.co.uk/careers/<id>/
            return HttpResponse(status=status.HTTP_204_NO_CONTENT)
        except Blogpost.DoesNotExist:
            return JsonResponse({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as exc:
            return JsonResponse({'detail': f'Error! Exception ocurred ({exc.__class__.__name__}): {exc}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
