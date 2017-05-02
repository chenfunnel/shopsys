from django.db import models

# Create your models here.

class Plan(models.Model):
    name=models.CharField("计划单名称",max_length=50)
    fromcity=models.CharField("出发城市",max_length=30, blank=False)
    tocity=models.CharField("目的城市",max_length=30,blank=False)
    start_at = models.DateField("出发日期",blank=False)
    back_at = models.DateField("返回日期",blank=False)
    traffictype=models.IntegerField("交通工具")
    hotletype=models.IntegerField("住宿")
    target=models.CharField("目标地址",max_length=50)
    targetcoordinate = models.CharField("目标地址坐标", max_length=60)
    ifback = models.BooleanField("是否往返", default=True)
    description=models.TextField("描述")
    is_active=models.IntegerField("计划状态",default=True)
    create_at = models.DateTimeField("创建时间", auto_now_add=True)
    update_at= models.DateTimeField("修改时间", auto_now=True)


    class Meta:
        db_table='plan'
        ordering=['-create_at']
        verbose_name = '计划'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name




class Plane_plan(models.Model):
    name = models.CharField("航班名称", max_length=50)
    companyname = models.CharField("航空公司", max_length=50)
    planetype = models.CharField("执行机型", max_length=50)
    fromcity = models.CharField("起飞站", max_length=30)
    tocity = models.CharField("落地站", max_length=30)
    start_at = models.DateTimeField("起飞时间")
    arrive_at = models.DateTimeField("落地时间")
    fromstation = models.CharField("起飞机场航站", max_length=50)
    tostation = models.CharField("落地机场航站", max_length=50)
    total_time=models.IntegerField("飞行时间")
    classtype=models.CharField("舱位", max_length=20)
    price=models.DecimalField("价格",max_digits=9,decimal_places=2,blank=True,default=0.00)
    description = models.TextField("描述")
    is_active = models.IntegerField("订购状态", default=True)
    create_at = models.DateTimeField("创建时间", auto_now_add=True)
    update_at = models.DateTimeField("修改时间", auto_now=True)
    planid=models.ForeignKey("Plan")

    class Meta:
        db_table = 'plane_plan'
        verbose_name = '飞机计划'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name



class Train_plan(models.Model):
    name = models.CharField("车次", max_length=50)
    traintype = models.CharField("火车类型", max_length=20)
    fromstation = models.CharField("出发站", max_length=30)
    tostation = models.CharField("到达站", max_length=30)
    start_at = models.DateTimeField("发车时间")
    arrive_at = models.DateTimeField("到站时间")
    total_time=models.IntegerField("行驶时间")
    classtype = models.CharField("席别", max_length=20)
    price=models.DecimalField("价格",max_digits=9,decimal_places=2,blank=True,default=0.00)
    description = models.TextField("描述")
    is_active = models.IntegerField("订购状态", default=True)
    create_at = models.DateTimeField("创建时间", auto_now_add=True)
    update_at = models.DateTimeField("修改时间", auto_now=True)
    planid=models.ForeignKey("Plan")

    class Meta:
        db_table = 'train_plan'
        verbose_name = '火车计划'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Hotel_plan(models.Model):
    name = models.CharField("宾馆名称", max_length=50)
    hoteltype = models.CharField("类型", max_length=20)
    address = models.CharField("地址", max_length=30)
    coordinate = models.CharField("地址坐标", max_length=60)
    classtype = models.CharField("房间类型", max_length=20)
    price=models.DecimalField("价格",max_digits=9,decimal_places=2,blank=True,default=0.00)
    start_at = models.DateField("入住日期")
    end_at = models.DateField("离店日期")
    total_time = models.IntegerField("住宿天数")
    description = models.TextField("描述")
    is_active = models.IntegerField("订购状态", default=True)
    create_at = models.DateTimeField("创建时间", auto_now_add=True)
    update_at = models.DateTimeField("修改时间", auto_now=True)
    planid=models.ForeignKey("Plan")

    class Meta:
        db_table = 'hotel_plan'
        verbose_name = '住宿计划'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

