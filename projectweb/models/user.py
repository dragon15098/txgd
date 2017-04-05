from mongoengine import *
class User(Document):
    username = StringField()
    password = StringField()
    token = StringField()
    image = FileField()
    number = StringField()
    address = StringField()
