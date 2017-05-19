# encoding:utf-8
from django import forms
from shopsys.apps.plan.models import Plan

# Create your views here.
#用户注册表单
class PlanForm(forms.Form):
    #name=forms.CharField(label="计划单名称",max_length=50)
    fromcity=forms.CharField(label="出发城市",max_length=30)
    tocity=forms.CharField(label="目的城市",max_length=30)
    start_at = forms.DateField(label="出发日期")
    back_at = forms.DateField(label="返回日期")
    traffictype=forms.IntegerField(label="交通工具")
    hotletype=forms.IntegerField(label="住宿")
    target=forms.CharField(label="目标地址",max_length=50)
    targetcoordinate = forms.CharField(label="目标地址坐标", max_length=60)
    ifback = forms.IntegerField(label="是否往返")
    description=forms.CharField(label="描述")
    #is_active=forms.IntegerField(label="计划状态")
#用户登录表单

class PlaneForm(forms.Form):
    name = forms.CharField(label="航班名称", max_length=50)
    companyname = forms.CharField(label="航空公司", max_length=50)
    planetype = forms.CharField(label="执行机型", max_length=50)
    fromcity = forms.CharField(label="起飞站", max_length=30)
    tocity = forms.CharField(label="落地站", max_length=30)
    start_at = forms.DateTimeField(label="起飞时间")
    arrive_at = forms.DateTimeField(label="落地时间")
    fromstation = forms.CharField(label="起飞机场航站", max_length=50)
    tostation = forms.CharField(label="落地机场航站", max_length=50)
    total_time = forms.IntegerField(label="飞行时间")
    classtype = forms.CharField(label="舱位", max_length=20)
    price = forms.DecimalField(label="价格", max_digits=9, decimal_places=2)
    description = forms.CharField(label="描述")

class TrainForm(forms.Form):
    name = forms.CharField(label="车次", max_length=50)
    traintype = forms.CharField(label="火车类型", max_length=20)
    fromstation = forms.CharField(label="出发站", max_length=30)
    tostation = forms.CharField(label="到达站", max_length=30)
    start_at = forms.DateTimeField(label="发车时间")
    arrive_at = forms.DateTimeField(label="到站时间")
    total_time = forms.IntegerField(label="行驶时间")
    classtype = forms.CharField(label="席别", max_length=20)
    price = forms.DecimalField(label="价格", max_digits=9, decimal_places=2)
    description = forms.CharField(label="描述")
    is_active = forms.BooleanField(label="订购状态")

class HotelForm(forms.Form):
    name = forms.CharField(label="宾馆名称", max_length=50)
    hoteltype = forms.CharField(label="类型", max_length=20)
    address = forms.CharField(label="地址", max_length=30)
    coordinate = forms.CharField(label="地址坐标", max_length=60)
    classtype = forms.CharField(label="房间类型", max_length=20)
    price = forms.DecimalField(label="价格", max_digits=9, decimal_places=2)
    start_at = forms.DateField(label="入住日期")
    end_at = forms.DateField(label="离店日期")
    total_time = forms.IntegerField(label="住宿天数")
    description = forms.CharField(label="描述")
    is_active = forms.BooleanField(label="订购状态")

class Plan_ContactForm(forms.Form):
    contact=forms.ChoiceField(label="乘机人")