from django.db import models
from member.models import Member

# Create your models here.
class Customer(models.Model):
    bno = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member,on_delete=models.SET_NULL, null=True)
    # id = models.CharField(max_length=50)
    btitle = models.CharField(max_length=1000)
    bcontent = models.TextField(blank=True)
    
    # 계층형 게시판 생성 시 필요
    bgroup = models.IntegerField(default=0)
    bstep = models.IntegerField(default=0)
    bindent = models.IntegerField(default=0)
    bhit = models.IntegerField(default=0)
    
    bfile1 = models.ImageField(null=True, blank=True,upload_to='customer')
    bfile2 = models.ImageField(null=True, blank=True,upload_to='customer')
    
    ntchk = models.IntegerField(default=0)
    bdate = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.bno} {self.btitle}"


# 다중파일 저장 시 테이블 분리   
# class customFile(models.Model):
#     fno = models.AutoField(primary_key=True)
#     customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

#     ffile = models.ImageField(null=True, blank=True,upload_to='board')
#     fdate = models.DateTimeField(auto_now=True)