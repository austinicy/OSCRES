from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50, default="unset")
    preferred_country =  models.CharField(max_length=50, default="unset")
    ielts_score = models.FloatField(max_length=50, default=0.0)


class University_Course(models.Model):
    name = models.CharField(max_length=50, default="unknown name")
    country = models.CharField(max_length=20, default="unknown country")
    city = models.CharField(max_length=20, default="unknown city")
    subject = models.CharField(max_length=50, default="unknown subject")
    min_ielts = models.FloatField(max_length=20, default=0.0)