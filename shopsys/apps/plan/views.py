from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from shopsys.apps.plan.forms import  PlanForm,PlaneForm,TrainForm,HotelForm
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from shopsys.apps.plan.models import Plan

# Create your views here.
def plan(request):
    Method = request.method

    if Method == 'POST':
        #如果有post提交的动作，就将post中的数据赋值给uf，供该函数使用

        uf = PlanForm(request.POST)
        print(uf)
        if uf.is_valid():
            print ('11')
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

            print (name)

            planAdd = Plan.objects.create(name=name,fromcity=fromcity,tocity=tocity,start_at=start_at,back_at=back_at,traffictype=traffictype,hotletype=hotletype,target=target,targetcoordinate=targetcoordinate,ifback=ifback,description=description,is_active=is_active)
            print(planAdd)
            return render (request,'plan/plan_detail.html',locals())

    else:
        uf = PlanForm()
    return render (request,'plan/plan.html',locals())

def planlist(request):
    Method = request.method
    if Method == 'POST':
        pass
    else:
        pass
    return render (request,'regist/regist.html',locals())