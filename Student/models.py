from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50, default="unset")
    preferred_country =  models.CharField(max_length=50, default="unset")
    ielts_score = models.FloatField(max_length=50, default=0.0)
