from mongoengine import *

class Number(Document):
    name = StringField()
    number = IntField()