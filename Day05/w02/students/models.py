from django.db import models

# Create your models here.

class Student(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    grade = models.IntegerField(default=0)
    gender = models.CharField(max_length=10)
    memo = models.TextField(blank=True)
    sdate = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"{self.no} {self.name}"