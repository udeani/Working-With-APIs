from django.shortcuts import render

from venv.I4G031137GJD.links.serizliers import LinkSerializer
from .models import Link
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView

# Create your views here.

class PostListApi(ListAPIView):
    queryset = Link.objects.filter(active=True)
    serializer_class = LinkSerializer

class PostCreateApi(CreateAPIView):
    queryset = Link.objects.filter(actvie=True)
    serializer_class = LinkSerializer

class PostDetailApi(RetrieveAPIView):
    queryset = Link.objects.filter(actvie=True)
    serializer_class = LinkSerializer

class PostUpdateApi(UpdateAPIView):
    queryset = Link.objects.filter(actvie=True)
    serializer_class = LinkSerializer

class PostDeleteApi(DestroyAPIView):
    queryset = Link.objects.filter(actvie=True)
    serializer_class = LinkSerializer