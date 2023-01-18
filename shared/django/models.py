from django.db.models import Model, DateTimeField, CharField, SlugField


class BaseModel(Model):
    createt_at = DateTimeField(auto_now_add=True)
    updatet_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class SlugBaseModel(Model):
    name = CharField(max_length=255)
    slug = SlugField(max_length=300,unique=True)

    class Meta:
        abstract = True
