from mongoengine import Document, StringField, IntField, DateTimeField, ListField
import datetime

class Song(Document):
    name = StringField(required=True, max_length=100)
    duration = IntField(required=True,min_value=0)
    uploaded_time = DateTimeField(default=datetime.datetime.now)

def _max_items(val):
    if len(val) > 10:
        raise ValidationError('List count can not be more than 10')

class Podcast(Document):
    name = StringField(required=True, max_length=100)
    duration = IntField(required=True, min_value=0)
    uploaded_time = DateTimeField(default=datetime.datetime.now)
    host = StringField(required=True, max_length=100)
    participants = ListField(StringField(max_length=100), validation=_max_items, default=list)

class Audiobook(Document):
    title = StringField(required=True, max_length=100)
    author = StringField(required=True, max_length=100)
    narrator = StringField(required=True, max_length=100)
    duration = IntField(required=True, min_value=0)
    uploaded_time = DateTimeField(default=datetime.datetime.now)

