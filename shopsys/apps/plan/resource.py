from django.core.urlresolvers import reverse
from rest_framework import serializers
from shopsys.apps.plan.models import Plane,Train,Hotel
from shopsys.apps.regist.models import Contact

class planserializer (serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = ['id', 'fromcity', 'tocity', 'name', 'companyname']

class trainserializer (serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = ['id', 'traintype', 'fromstation', 'name', 'tostation']

class hotelserializer (serializers.ModelSerializer):
    class Meta:
        model = Train
        fields = ['id', 'hoteltype', 'city', 'name', 'address','classtype']

class contactserializer(serializers.ModelSerializer):
    class  Meta:
        model= Contact
        fields=['id','name','cardid','telephone','weixin','age','sex','description','is_active','customer']

