# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Favorite(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    vehicle = models.ForeignKey('Vehicle', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'favorite'


class User(models.Model):
    username = models.CharField(unique=True, max_length=16)
    password = models.CharField(max_length=32)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Vehicle(models.Model):
    icao24 = models.CharField(unique=True, max_length=6, blank=True, null=True)
    callsign = models.CharField(unique=True, max_length=45, blank=True, null=True)
    origin_country = models.CharField(max_length=45, blank=True, null=True)
    on_ground = models.IntegerField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    velocity = models.FloatField(blank=True, null=True)
    category = models.IntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'vehicle'
