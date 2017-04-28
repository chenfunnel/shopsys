# encoding:utf-8
from django import forms
from shopsys.apps.plan.models import Plan,Scheme

# Create your views here.
#用户注册表单
class PlanForm(forms.Form):
    name=forms.CharField("计划单名称",max_length=50)
    fromcity=forms.CharField("出发城市",max_length=30, blank=False,error_messages={'required': '出发城市不能为空', 'invalid': '格式错误'})
    toctiy=forms.CharField("目的城市",max_length=30,blank=False,error_messages={'required': '目标城市不能为空', 'invalid': '格式错误'})
    start_at = forms.DateField("出发日期",blank=False,error_messages={'required': '出发日期不能为空', 'invalid': '格式错误'})
    back_at = forms.DateField("返回日期",blank=False,error_messages={'required': '返回日期不能为空', 'invalid': '格式错误'})
    traffictype=forms.IntegerField("交通工具")
    hotletype=forms.IntegerField("住宿")
    target=forms.CharField("目标地址",max_length=50)
    targetcoordinate = forms.CharField("目标地址坐标", max_length=60)
    ifback = forms.BooleanField("是否往返", default=True)
    description=forms.TextField("描述")
    is_active=forms.BooleanField("计划状态",default=True)
#用户登录表单
class ShemeForm(forms.Form):
    name = forms.CharField("方案名称", max_length=50)
    traffictype = forms.IntegerField("交通工具")
    hotletype = forms.IntegerField("住宿")
    start_at = forms.DateTimeField("出发时间")
    arrive_at = forms.DateTimeField("到达时间")
    total_time=forms.IntegerField("总时间")
    total_fee=forms.DecimalField("总费用",max_digits=9,decimal_places=2,blank=True,default=0.00)
    description = forms.TextField("描述")
    is_active = forms.BooleanField("方案状态", default=True)


class PlaneForm(forms.Form):
    name = forms.CharField("航班名称", max_length=50)
    companyname = forms.CharField("航空公司", max_length=50)
    planetype = forms.CharField("执行机型", max_length=50)
    fromcity = forms.CharField("起飞站", max_length=30)
    tocity = forms.CharField("落地站", max_length=30)
    start_at = forms.DateTimeField("起飞时间", auto_now_add=True)
    arrive_at = forms.DateTimeField("落地时间", auto_now_add=True)
    fromstation = forms.CharField("起飞机场航站", max_length=50)
    tostation = forms.CharField("落地机场航站", max_length=50)
    total_time = forms.IntegerField("飞行时间")
    classtype = forms.CharField("舱位", max_length=20)
    price = forms.DecimalField("价格", max_digits=9, decimal_places=2, blank=True, default=0.00)
    description = forms.TextField("描述")

class TrainForm(forms.Form):
    name = forms.CharField("车次", max_length=50)
    traintype = forms.CharField("火车类型", max_length=20)
    fromstation = forms.CharField("出发站", max_length=30, unique=True)
    tostation = forms.CharField("到达站", max_length=30, unique=True)
    start_at = forms.DateTimeField("发车时间", auto_now_add=True)
    arrive_at = forms.DateTimeField("到站时间", auto_now_add=True)
    total_time = forms.IntegerField("行驶时间")
    classtype = forms.CharField("席别", max_length=20)
    price = forms.DecimalField("价格", max_digits=9, decimal_places=2, blank=True, default=0.00)
    description = forms.TextField("描述")
    is_active = forms.BooleanField("订购状态", default=True)

class HotelForm(forms.Form):
    name = forms.CharField("宾馆名称", max_length=50)
    hoteltype = forms.CharField("类型", max_length=20)
    address = forms.CharField("地址", max_length=30, unique=True)
    coordinate = forms.CharField("地址坐标", max_length=60)
    classtype = forms.CharField("房间类型", max_length=20)
    price = forms.DecimalField("价格", max_digits=9, decimal_places=2, blank=True, default=0.00)
    start_at = forms.DateField("入住日期", auto_now_add=True)
    end_at = forms.DateField("离店日期", auto_now_add=True)
    total_time = forms.IntegerField("住宿天数")
    description = forms.TextField("描述")
    is_active = forms.BooleanField("订购状态", default=True)