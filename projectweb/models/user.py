from mongoengine import *

class User(Document):
    username = StringField()
    password = StringField()
    gender = StringField()
    description = StringField()
    number = IntField()
    image = StringField()
    token = StringField()
