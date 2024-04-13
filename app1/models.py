from django.db import models

# Create your models here.
class Marks(models.Model):
    credit=models.IntegerField(max_length=2)
    score=models.IntegerField(max_length=2)
class Marks1(models.Model):
    gpa=models.FloatField(max_length=4)