from django.db import models

# Create your models here.

class Student(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    kor = models.IntegerField(default=0)
    eng = models.IntegerField(default=0)
    math = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    avg = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.no} {self.name}"
    
class Student2(models.Model):
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    grade= models.IntegerField(default=0)
    gender = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.name} {self.major}"