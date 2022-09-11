from mongoengine import fields

from library.model import BaseModel, BaseQuerySet


class ExampleManager(BaseQuerySet):
    pass


class ExampleModel(BaseModel):
    name = fields.StringField(default = 'name', required = True)

    objects: ExampleManager

    meta = {
        'collection': 'example_data',
        'queryset_class': ExampleManager
    }
