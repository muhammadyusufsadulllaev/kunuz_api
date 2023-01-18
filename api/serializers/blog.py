from rest_framework.fields import HiddenField, CurrentUserDefault
from rest_framework.serializers import ModelSerializer

from api.models.blog import Category, Region, Blog


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        exclude = ('slug',)


class RegionSerializer(ModelSerializer):
    class Meta:
        model = Region
        exclude = ('slug',)


class BlogSerializer(ModelSerializer):
    author = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Blog
        exclude = ('slug',)


