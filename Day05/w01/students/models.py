from django.db import models

# Create your models here.

class Student(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    grade =  models.IntegerField(default=0)
    age =  models.IntegerField(default=0)
    gender = models.CharField(max_length=10, blank=True)
    hobby = models.CharField(max_length=100, blank=True)
    sdate = models.DateTimeField(auto_now=True) #date-sysdate
    memo = models.TextField(blank = True) #clob
    
    def __str__(self):
        return f"{self.no} {self.name} {self.sdate}"