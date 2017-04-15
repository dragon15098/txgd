from mongoengine import *

class UserFemale(Document):
    username = StringField()
    password = StringField()
    token = StringField()

    description = StringField()
