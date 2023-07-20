from django.db import models
from django.db.models import Max

class Student(models.Model):
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    gpa = models.IntegerField(null=True)
    
    def __str__(self):
        return self.fname

