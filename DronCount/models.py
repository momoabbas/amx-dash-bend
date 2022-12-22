from django.db import models
from django.contrib.auth.models import User
# from django_google_maps import fields as map_fields
import sys
from datetime import datetime
# from django.contrib.gis.db import models

class CountDetails(models.Model):
    annotation_name = models.CharField(max_length=50, null=True, blank=True)
    video = models.FileField(upload_to="media",null= True)
    # annotation=models.CharField(upload_to="media",null= True)

    # geolocation = map_fields.GeoLocationField(max_length=100)



    # geom = models.PointField(blank=True, null=True)

class Drone(models.Model):
    model_name=models.CharField(max_length=50, null=True, blank=True)
    UIN=models.CharField(max_length=50, null=True, blank=True)
    time_in_service=models.DateTimeField(verbose_name="Time in service",blank=True,null=True)
    Next_maintainance=models.DateTimeField(verbose_name="Next_maintainance",blank=True,null=True)
    purchase_year=models.DateTimeField(verbose_name="purchase_year",blank=True,null=True)
    # purchase_day=models.FloatField(null=True, blank=True)
    # purchase_month=models.FloatField(null=True, blank=True)
    # drone_location=models.CharField(max_length=50, null=True, blank=True)
    aircraft_type=models.CharField(max_length=50, null=True, blank=True)
    connection_id=models.CharField(max_length=50, null=True, blank=True)
    created_timestamp =models.DateTimeField(auto_now_add=True,verbose_name="Created_Timestamp",blank=True,null=True)
    last_update_timestamp= models.DateTimeField(auto_now_add=True,verbose_name="last_update_timestamp",blank=True, null=True)
# date=Drone.data.purchase_year.date()
class GMap(models.Model):
    # geolocation = map_fields.GeoLocationField(max_length=100)
    drone = models.ForeignKey(Drone,null=True, on_delete= models.CASCADE)
    lng=models.CharField(max_length=50, null=True, blank=True)
    lat=models.CharField(max_length=50, null=True, blank=True)
    isActive=models.BooleanField(default=False)
    # is_on=models.BooleanField(default=False)



class Log(models.Model):
    logData=models.FileField(upload_to="media",null= True)
