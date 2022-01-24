from django.db import models
from django.db.models.fields import *
from sqlalchemy import VARCHAR, ForeignKey

class User(models.Model):
    user_name = CharField(max_length=50)
    email = CharField(max_length=100)
    user_phone = CharField(max_length=11)
    user_addr = CharField(max_length=250)
    profile_img = TextField(blank=True)
    def __str__(self):
        return self.user_name


class Pet(models.Model):
    pet_name = CharField(max_length=50)
    gender = CharField(max_length=1, null=True, blank=True)
    age = IntegerField(null=True, blank=True)
    size = CharField(max_length=1, null=True, blank=True)
    neutered = CharField(max_length=1, null=True, blank=True)
    pet_img = TextField(blank=True)
    user_id = models.ForeignKey(User, db_column='user_id', on_delete = models.SET_NULL, null=True)

    def __str__(self):
        return self.pet_name