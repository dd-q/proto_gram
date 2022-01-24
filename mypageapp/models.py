from django.db import models
from django.db.models.fields import *

class User(models.Model):
    name = CharField(max_length=50)
    email = CharField(max_length=100)
    phone = CharField(max_length=11)
    address = CharField(max_length=250)
    profile_photo = TextField(blank=True)
    def __str__(self):
        return self.name


class Pet(models.Model):
    pet_name = CharField(max_length=50)
    mf = BooleanField()
    age = IntegerField()
    sort = BooleanField()
    nt = BooleanField()
    pet_profile_photo = TextField(blank=True)

    def __str__(self):
        return self.name