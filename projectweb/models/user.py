from mongoengine import *

class User(Document):
    username = StringField()
    password = StringField()
    token = StringField()
    gender = StringField()
    description = StringField()
    number = IntField()
    image = StringField()
