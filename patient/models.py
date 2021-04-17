from django.db import models

# Create your models here.
class patient(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    #date=models.DateField()
class predictions(models.Model):
    gender = models.IntegerField()
    age = models.IntegerField()
    smoking = models.IntegerField()
    yellow_fingers = models.IntegerField()
    anxiety =models.IntegerField()
    peer_pressure = models.IntegerField()
    chronic_disease = models.IntegerField()
    fatigue =models.IntegerField()
    allergy = models.IntegerField()
    wheezing = models.IntegerField()
    alcohol_consuming = models.IntegerField()
    coughing = models.IntegerField()
    shortness_of_breath = models.IntegerField()
    swallowing_difficulty = models.IntegerField()
    chest_pain = models.IntegerField()
    lung_cancer= models.IntegerField()

