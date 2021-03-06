"""This is the database models, built with mongoengine, an ODM client for Mongodb"""

from mongoengine import Document, StringField, IntField, DateTimeField, ListField
import datetime


"""Creating the models for audio file type Song"""
class Song(Document):
    name = StringField(required=True, max_length=100)
    duration = IntField(required=True,min_value=0)
    uploaded_time = DateTimeField(default=datetime.datetime.now)


"""Creating a custom validation for ListField in Podcast.participants"""
def _max_items(val):
    if len(val) > 10:
        raise ValidationError('List count can not be more than 10')


"""Creating the models for audio file type Podcast"""
class Podcast(Document):
    name = StringField(required=True, max_length=100)
    duration = IntField(required=True, min_value=0)
    uploaded_time = DateTimeField(default=datetime.datetime.now)
    host = StringField(required=True, max_length=100)
    participants = ListField(StringField(max_length=100), validation=_max_items, default=list)


"""Creating the models for audio file type Audiobook"""
class Audiobook(Document):
    title = StringField(required=True, max_length=100)
    author = StringField(required=True, max_length=100)
    narrator = StringField(required=True, max_length=100)
    duration = IntField(required=True, min_value=0)
    uploaded_time = DateTimeField(default=datetime.datetime.now)

