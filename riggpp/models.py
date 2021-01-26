from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=64)
    age=models.IntegerField()
    location=models.CharField(max_length=64)
