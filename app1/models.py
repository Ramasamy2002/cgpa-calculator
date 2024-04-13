from django.db import models

# Create your models here.
class Marks(models.Model):
    session_id = models.CharField(max_length=40,default=" ") 
    credit=models.IntegerField(max_length=2)
    score=models.IntegerField(max_length=2)
class Marks1(models.Model):
    session_id = models.CharField(max_length=40,default=" ")
    gpa=models.FloatField(max_length=4)