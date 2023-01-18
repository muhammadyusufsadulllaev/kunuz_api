from graphene_django import DjangoObjectType
import graphene

from api.models.blog import Blog


class BLogs(DjangoObjectType):
    class Meta:
        model = Blog


class Query(graphene.ObjectType):
    blogs = graphene.List(BLogs)

    @graphene.resolve_only_args
    def resolve_blogs(self):
        return Blog.objects.all()


schema = graphene.Schema(query=Query)
