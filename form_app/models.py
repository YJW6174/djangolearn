#coding:utf-8
from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField('姓名',max_length=50)
    password = models.CharField(max_length=50)


    def __unicode__(self):
        return self.username
SEX_CHOICES = (
    ('0','男'),
    ('1','女'),
)
UserWork_CHOICES = (
    ('0','学生'),
    ('1','老师'),
)

class student(models.Model):
    acaname=models.CharField('学_院',max_length=50)
    classnum=models.CharField('班_级',max_length=50)
    stuid=models.CharField('学_号',max_length=50)
    username=models.CharField('姓_名',max_length=50)
    sex = models.CharField('性_别',choices = SEX_CHOICES,max_length = 1)
    userwork=models.CharField('职_业',choices = UserWork_CHOICES,max_length = 1)

class grade(models.Model):
    acaname=models.CharField('学_院',max_length=50)
    stuid=models.CharField('学_号',max_length=50)
    username=models.CharField('姓_名',max_length=50)
    grade1=models.CharField('英_语',max_length=50)
    grade2 = models.CharField('高_数',max_length=50)
    grade3=models.CharField('大_物',max_length=50)

