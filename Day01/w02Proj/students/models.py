from django.db import models

# Create your models here.
# Class 객체 등록하면 DB 자동 생성

# 오라클 table 생성 코드
# create table student (
#     name varchar2(100),
#     major varchar2(100),
#     age number(3),
#     grade number(1),
#     gender varchar2(6),
# )

class Student(models.Model):
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    grade = models.IntegerField(default=1)
    gender = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name+", "+self.major