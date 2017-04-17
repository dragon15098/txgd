from mongoengine import *

class Number(Document):
    name = StringField()
    numberboy = IntField()
    numbergirl = IntField()