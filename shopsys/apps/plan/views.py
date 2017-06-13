from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from shopsys.apps.plan.forms import  PlanForm,PlaneForm,TrainForm,HotelForm,Plan_ContactForm
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect,JsonResponse
from shopsys.apps.plan.models import Plan,Plane_plan,Hotel_plan,Train_plan,Train,Hotel,Plane
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from shopsys.apps.regist.models import Contact
from rest_framework.views import APIView
from rest_framework.response import Response
from shopsys.apps.plan.resource import planserializer,trainserializer,hotelserializer,contactserializer
from rest_framework.decorators import api_view
from django.views.generic import View
from rest_framework import  status
from rest_framework import generics

# Create your views here.
@login_required
def plan(request):
    username = request.session.get('username', default=None)


    Method = request.method
    if Method == 'POST':
        #如果有post提交的动作，就将post中的数据赋值给uf，供该函数使用

        uf = PlanForm(request.POST)

        if uf.is_valid():
            name=uf.cleaned_data['fromcity']+uf.cleaned_data['tocity']+uf.cleaned_data['start_at'].strftime("%Y%m%d")
            fromcity = uf.cleaned_data['fromcity']
            tocity = uf.cleaned_data['tocity']
            start_at=uf.cleaned_data['start_at']
            back_at = uf.cleaned_data['back_at']
            traffictype = uf.cleaned_data['traffictype']
            hotletype = uf.cleaned_data['hotletype']
            target = uf.cleaned_data['target']
            targetcoordinate = uf.cleaned_data['targetcoordinate']
            ifback = uf.cleaned_data['ifback']
            description = uf.cleaned_data['description']
            is_active=1
            customerid=request.session.get('userid', default=1)
            #customerid=1

            planAdd = Plan.objects.create(name=name,fromcity=fromcity,tocity=tocity,start_at=start_at,back_at=back_at,traffictype=traffictype,hotletype=hotletype,target=target,targetcoordinate=targetcoordinate,ifback=ifback,description=description,is_active=is_active,customer_id=customerid)
            response = HttpResponseRedirect('/plan/plandetail/?planid='+str(planAdd.id))
            return response

            #return HttpResponse('/plan/plandetail/?planid='+str(planAdd.id))
            #return render (request,'plan/plan_detail.html',locals())

    else:
        uf = PlanForm()
    return render (request,'plan/plan.html',locals())

@login_required
def planlist(request):
    username = request.session.get('username', default=None)
    customerid = request.session.get('userid', default=None)
    plan_list=Plan.objects.filter(customer_id=customerid).order_by("-id")
    paginator = Paginator(plan_list, 6)
    page = request.GET.get('page')
    try:
        plans = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        plans = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        plans = paginator.page(paginator.num_pages)
    return render (request,'plan/planlist.html',locals())

@login_required
def plandetail(request):
    planid = request.GET.get('planid')
    username = request.session.get('username', default=None)
    customerid = request.session.get('userid', default=None)
    plan=Plan.objects.get(id=planid)
    fromcity=plan.fromcity
    tocity=plan.tocity
    planes=Plane.objects.filter(fromcity=fromcity, tocity=tocity)
    trains=Train.objects.filter(fromstation=fromcity,tostation=tocity)
    hotels=Hotel.objects.filter(city=tocity)
    contacts=Contact.objects.filter(customer=customerid)
    return render (request,'plan/plan_detail_3.html',locals())

def get_contact(request):
    r = [('', '----')]
    customerid = request.session.get('userid', default=None)
    contact_list = Contact.objects.filter(customer_id=customerid)
    for obj in contact_list:
       r = r + [(obj.id, obj.name)]
    return r
#飞机

#飞机列表类
class Cart_plane(object):
    def __init__(self, *args, **kwargs):
        self.items = []

    def add_plane(self,plan,plane):
        contact_list=plan.contact.all()
        for item in contact_list:
            self.items.append(Plane(id=plane.id, planid=plan.id,contactid=item.customer_id))
        print (self.items)
        return  self.items

#显示飞机票购物车
def view_cartplane(request):
    cart_plane = request.session.get("cart_plane",None)
    if not cart_plane:
        cart_plane = Cart_plane()
        request.session["cart_plane"] = cart_plane
    return render(request,'plan/plan_detail_2.html',locals())

#添加到飞机票购物车
def add_to_cartplane(request,id):
    plane = Plane.objects.get(id = id)
    planid = request.GET.get('planid')
    plan= Plan.objects.get(id=planid)
    cart = request.session.get("cart_plane",None)
    if not cart:
        cart = Cart_plane()
        request.session["cart_plane"] = cart
        cart.add_plane(plane,plan)
        request.session['cart_plane'] = cart
    return view_cartplane(request)

#清空飞机票购物车
def clean_cartplane(request):
    request.session["cart_plane"] = Cart_plane()
    return view_cartplane(request)

#火车
#火车列表类
class Cart_train(object):
    def __init__(self, *args, **kwargs):
        self.items = []

    def add_train(self,plan,train):
        contact_list=plan.contact.all()
        for item in contact_list:
            self.items.append(Train(id=train.id, planid=plan.id,contactid=item.customer_id))
        print (self.items)
        return  self.items

#显示火车票购物车
def view_carttrain(request):
    cart_train = request.session.get("cart_train",None)
    if not cart_train:
        cart_train = Cart_train()
        request.session["cart_train"] = cart_train
    return render(request,'plan/plan_detail.html',locals())

#添加到火车票购物车
def add_to_carttrain(request,id):
    train = Train.objects.get(id = id)
    planid = request.GET.get('planid')
    plan = Plan.objects.get(id=planid)
    cart = request.session.get("cart_train",None)
    if not cart:
        cart = Cart_train()
        request.session["cart_train"] = cart
        cart.add_train(train,plan)
        request.session['cart_train'] = cart
    return view_carttrain(request)

#清空火车票购物车
def clean_carttrain(request):
    request.session["cart_train"] = Cart_train()
    return view_carttrain(request)

#宾馆
#宾馆列表类
class Cart_hotel(object):
    def __init__(self, *args, **kwargs):
        self.items = []

    def add_hotel(self,plan,hotel):
        contact_list=plan.contact.all()
        for item in contact_list:
            self.items.append(Hotel(id=hotel.id, planid=plan.id,contactid=item.customer_id))
        print (self.items)
        return  self.items

#显示宾馆购物车
def view_carthotel(request):
    cart_hotel = request.session.get("cart_hotel",None)
    if not cart_hotel:
        cart_hotel = Cart_hotel()
        request.session["cart_hotel"] = cart_hotel
    return render(request,'plan/plan_detail.html',locals())

#添加到宾馆购物车
def add_to_carthotel(request,id):
    hotel = Hotel.objects.get(id = id)
    planid = request.GET.get('planid')
    plan = Plan.objects.get(id=planid)
    cart = request.session.get("cart_hotel",None)
    if not cart:
        cart = Cart_hotel()
        request.session["cart_hotel"] = cart
        cart.add_hotel(hotel,plan)
        request.session['cart_hotel'] = cart
    return view_carthotel(request)

#清空宾馆购物车
def clean_carthotel(request):
    request.session["cart_hotel"] = Cart_hotel()
    return view_carthotel(request)


class PlaneList(APIView):
    def get(self, request, format=None):
        planes = Plane.objects.all()
        plansserializer = planserializer(planes, many=True)
        return Response(plansserializer.data)

class TrainList(APIView):
    def get(self, request, format=None):
        trains = Train.objects.all()
        trainsserializer = trainserializer(trains, many=True)
        return Response(trainsserializer.data)

class HotelList(APIView):
    def get(self, request, format=None):
        hotels = Hotel.objects.all()
        hotelsserializer = hotelserializer(hotels, many=True)
        return Response(hotelsserializer.data)

plan_field_list = ['id', 'plan_id', {'contact': ['id', 'name']}]
#获取当前用户的联系人列表
class contactlist(APIView):
    def get(self, request, format=None):
        customerid = request.session.get('userid', default=None)
        #contacts = Contact.objects.filter(customer=customerid)
        contacts = Contact.objects.all()
        serializer = contactserializer(contacts, many=True)
        return Response(serializer.data)
    def post(self,request,format=None):
        customer_list=request.POST.getlist('chk')
        planid=request.POST.get('planid')
        plan=Plan.objects.get(id=planid)
        plan.contact.clear()
        plan.contact.add(*customer_list)
        contact=plan.contact.all()
        serializer = contactserializer(contact, many=True)
        return Response(serializer.data)


class contactview(View):
    def get(self, request):
        _list = Plan.objects.all()
        _rtn = [i.serializable_values(plan_field_list) for i in _list]
        result = {"data": _rtn}
        return JsonResponse(result)


#获取某个联系人操作
@api_view(['GET','PUT','DELETE'])
def contact_detail(request,pk):
    try:
        contacts = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = contactserializer(contacts)
        return Response(serializer.data)
    elif request.method=='PUT':
        serializer = contactserializer(contacts,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        contacts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

