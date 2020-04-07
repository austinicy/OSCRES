from django.db import models

class University_Course(models.Model):
    name = models.CharField(max_length=50, defult="unknown name")
    country = models.CharField(max_length=20, defult="unknown country")
    city = models.CharField(max_length=20, defult="unknown city")
    subject = models.CharField(max_length=50, defult="unknown subject")
    min_ietls = models.CharField(max_length=20, default="0.0")
