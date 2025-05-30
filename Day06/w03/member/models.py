from django.db import models

# Create your models here.

class Member(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    pw = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    nickName = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    hobby = models.CharField(max_length=50)
    mdate = models.DateTimeField(auto_now=False, null=True)
    
    def __str__(self):
        return f"{self.id} {self.name}"
    
    
    
    
    
    