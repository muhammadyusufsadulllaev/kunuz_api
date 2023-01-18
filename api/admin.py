from django.contrib import admin
from django.contrib.admin import ModelAdmin

from api.models.blog import Blog


# Register your models here.
@admin.register(Blog)
class BlogAdmin(ModelAdmin):
    pass
