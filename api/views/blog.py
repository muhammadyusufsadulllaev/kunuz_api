from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from api.filter import TagFilter
from api.models.blog import Category, Region, Blog
from api.serializers.blog import CategorySerializer, RegionSerializer, BlogSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TagFilter





