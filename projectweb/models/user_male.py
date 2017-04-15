from mongoengine import *

class UserMale(Document):
    username = StringField()
    password = StringField()
    token = StringField()
    description = StringField()



