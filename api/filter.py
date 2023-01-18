from django_filters import FilterSet, filters

from api.models.blog import Blog


class TagFilter(FilterSet):
    tags = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Blog
        fields = ('category', 'region', 'tags')
