from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    name=models.CharField("姓名",max_length=50)
    loginname=models.CharField("登录名",max_length=30,unique=True)
    password=models.CharField("密码",max_length=30)
    telephone=models.CharField("手机",max_length=30)
    weixin=models.CharField("微信号",max_length=50)
    description=models.TextField("描述")
    is_active=models.BooleanField("是否有效",default=True)
    regist_at=models.DateTimeField("注册时间",auto_now_add=True)
    update_at=models.DateTimeField("修改时间",auto_now=True)

    class Meta:
        db_table='customer'
        ordering=['-regist_at']
        verbose_name = '客户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('regist_customer',args=(self.slug,))

class Contact(models.Model):
    name = models.CharField("姓名", max_length=50)
    cardid = models.CharField("身份证号", max_length=30)
    telephone = models.CharField("手机", max_length=30)
    weixin = models.CharField("微信号", max_length=50)
    age=models.IntegerField("年龄")
    sex=models.IntegerField("性别",choices=((1,'男'),(0,'女'),))
    description = models.TextField("描述")
    is_active = models.BooleanField("是否有效", default=True)
    create_at = models.DateTimeField("新增时间", auto_now_add=True)
    update_at = models.DateTimeField("修改时间", auto_now=True)
    customer=models.ForeignKey(User)

    class Meta:
        db_table = 'contact'
        ordering = ['-create_at']
        verbose_name = '联系人'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('regist_contact', args=(self.slug,))