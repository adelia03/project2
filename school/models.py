from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=70)
    age = models.IntegerField()
    grade = models.IntegerField()
