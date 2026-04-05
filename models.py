from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address= models.CharField(max_length=300)
    gender= models.CharField(max_length=30)


class traffic_accident_detection(models.Model):

    Fid = models.CharField(max_length=100)
    Accident_Index = models.CharField(max_length=100)

    Longitude = models.FloatField()
    Latitude = models.FloatField()

    Police_Force = models.CharField(max_length=100)
    Accident_Severity = models.CharField(max_length=100)

    Number_of_Vehicles = models.IntegerField()
    Number_of_Casualties = models.IntegerField()

    ADate = models.CharField(max_length=20)
    Day_of_Week = models.CharField(max_length=50)
    ATime = models.CharField(max_length=20)

    first_Road_Class = models.CharField(max_length=100)
    first_Road_Number = models.CharField(max_length=100)

    Road_Type = models.CharField(max_length=100)
    Speed_limit = models.IntegerField()

    Junction_Control = models.CharField(max_length=100)

    second_Road_Class = models.CharField(max_length=100)
    second_Road_Number = models.CharField(max_length=100)

    Light_Conditions = models.CharField(max_length=100)
    Weather_Conditions = models.CharField(max_length=100)
    Road_Surface_Conditions = models.CharField(max_length=100)

    Prediction = models.TextField()

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)



