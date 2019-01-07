from django.db import models

# Create your models here.
from django import forms
from django.contrib.auth.models import User
from django.utils import timezone


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

#error
# class UserProfile (models.Model):
#     user = models.OneToOneField(User,unique=True,on_delete=models.CASCADE)
#     birth = models.DateField(blank=True,null=True)
#     phone = models.CharField(max_length=20,null=True)
#
#     def __str__(self):
#         return 'user{}'.format(self.user.username)

class UserProfiles (models.Model):
    user = models.OneToOneField(User,unique=True,on_delete=models.CASCADE)
    birth = models.DateField(blank=True,null=True,)
    phone = models.CharField(max_length=20,null=True)

    def __str__(self):
        return 'user{}'.format(self.user.username)

#   个人信息
#   on_delete=models.CASCADE  不可缺少，
#   在django2.0后，定义外键和一对一关系的时候需要加on_delete选项，此参数为了避免两个表里的数据不一致问题
class UserInfo (models.Model):
    user = models.OneToOneField(User,unique=True,on_delete=models.CASCADE)
    school = models.CharField(max_length=100,blank=True)
    company = models.CharField(max_length=100,blank=True)   #工作单位
    profession = models.CharField(max_length=100, blank=True)   #职业
    address = models.CharField(max_length=100, blank=True)
    aboutme = models.TextField(blank=True)   #个人介绍
    photo =models.ImageField(blank=True)    #图片 blank=True可以为空

    def __str__(self):
        return 'user{}'.format(self.user.username)