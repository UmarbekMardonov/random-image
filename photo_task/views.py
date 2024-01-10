from django.shortcuts import render
from .models import ImageModel
from .utils import download_image
from rest_framework import generics, status
from .serializers import ImageSerializers
from rest_framework.response import Response
import datetime


class ImagesList(generics.ListAPIView):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializers


class ImagesCreate(generics.GenericAPIView):
    def get(self, request):
        start = datetime.datetime.now()
        download_image.delay()
        end = datetime.datetime.now()
        print(end - start)
        return Response(status=status.HTTP_200_OK)
