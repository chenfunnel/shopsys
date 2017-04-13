from django.shortcuts import render,get_object_or_404
from .forms import  CustomerForm
from django.http import HttpRequest,HttpResponse

# Create your views here.

def index(request):
    page_title='注册'
    return render(request,'regist/index.html',locals())

def add_regist(request):
    page_title = '新增注册'
    if request.method == "POST":
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer_form.save()
        return HttpResponse("注册信息提交完成")

    else:
        customer_form = CustomerForm
    return render(request,'regist/register.html',locals())
