from ckeditor.fields import RichTextField
from django.contrib.postgres.fields import ArrayField
from django.db.models import CharField, ForeignKey, CASCADE
from django.utils.text import slugify


from shared.django.models import BaseModel, SlugBaseModel
from users.models import User


class Category(BaseModel, SlugBaseModel):

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        while Category.objects.filter(slug=self.slug).exists():
            self.slug += str(Category.objects.filter(slug=self.slug).count())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Region(BaseModel, SlugBaseModel):

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        while Region.objects.filter(slug=self.slug).exists():
            self.slug += str(Region.objects.filter(slug=self.slug).count())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Blog(BaseModel, SlugBaseModel):
    category = ForeignKey(Category, CASCADE)
    region = ForeignKey(Region, CASCADE)
    description = CharField(max_length=255)
    text = RichTextField()
    tags = ArrayField(CharField(max_length=10, blank=True), size=8)
    author = ForeignKey(User, CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        while Blog.objects.filter(slug=self.slug).exists():
            self.slug += str(Blog.objects.filter(slug=self.slug).count())
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
