from django.db import models
from member.models import Member

# Create your models here.

class Board(models.Model):
    bno = models.AutoField(primary_key=True) # 게시판 번호
    id = models.CharField(max_length=100) #작성자
    # 외래키(Foreign Key)
    member = models.ForeignKey(Member, on_delete=models.DO_NOTHING)
    btitle = models.CharField(max_length=1000) #제목
    bcontent = models.TextField() #내용
    # 답글 달기
    bgroup = models.IntegerField(default=0) #답글달기 묶음
    bstep = models.IntegerField(default=0) #답글달기 순서
    bindent = models.IntegerField(default=0) #들여쓰기
    # --- 
    bhit = models.IntegerField(default=0)
    bfile = models.ImageField(upload_to='board', null=True, blank=True)
    bdate = models.DateTimeField(auto_now=True)
    ntchk = models.IntegerField(default='')
    def __str__(self):
        return f"{self.bno} {self.id} {self.btitle}"