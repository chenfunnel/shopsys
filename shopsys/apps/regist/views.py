from django.shortcuts import render,get_object_or_404
from .forms import  ContactForm,UserForm,LoginForm
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from shopsys.apps.regist.models import Customer,Contact
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required


# Create your views here.

# def add_regist(request):
#     page_title = '新增注册'
#     if request.method == "POST":
#         customer_form = CustomerForm(request.POST)
#         if customer_form.is_valid():
#             customer_form.save()
#         return HttpResponse("注册信息提交完成")
#
#     else:
#         customer_form = CustomerForm
#     return render(request,'regist/register.html',locals())

def regist(request):
    Method = request.method
    if Method == 'POST':
        #如果有post提交的动作，就将post中的数据赋值给uf，供该函数使用
        uf = UserForm(request.POST)
        if uf.is_valid():

            email=uf.cleaned_data['email']
            username = uf.cleaned_data['username']
            password1 = uf.cleaned_data['password1']
            password2 = uf.cleaned_data['password2']
            errors=[]
            #判断密码是否一致
            if password1==password2 :
                password=password2
            else:
                errors.append("两次输入的密码不一致!")
                return render(request, 'regist/regist.html', locals())
            #try:
            # registJudge = Customer.objects.filter(loginname = username)
            # if len(registJudge)>0 :
            #     errors.append("该用户已存在，请重新填写")
            #     return render(request,'regist/regist.html',locals())
            # #except :
            # if not errors:
            #     registAdd = Customer.objects.create(name=name,loginname=username,password=password)
            user=User.objects.create_user(username,email,password)
            response = HttpResponseRedirect('/regist/')
            return response
    else:
        uf = UserForm()
    return render (request,'regist/regist.html',locals())
#切换到Django默认的认证方式
#
def login(request):

    if request.method == 'POST':
        uf = LoginForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #对比输入的用户名和密码和数据库中是否一致
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                user_list = User.objects.get(username=username)

            #if userPassJudge:
                request.session['username'] = username
                request.session['userid']=user_list.id
                response = HttpResponseRedirect('/regist/')
                return response
            else:
                return render(request, 'regist/login.html', locals())
    else:
        uf = LoginForm()
    return render(request,'regist/login.html',locals())


def index(request):
    username = request.session.get('username', default=None)
    return render(request,'regist/dashboard.html',locals())

@login_required
def logout_view(request):
    logout(request)
    #del request.session['username']
    #del request.session['userid']
    response = HttpResponseRedirect('/regist/')
    return  response

def user(request):
    username = request.session.get('username', default=None)
    return render(request,'regist/user.html',locals())

def maps(request):
    username = request.session.get('username', default=None)
    return render(request,'regist/maps.html',locals())

def notificaiton(request):
    username = request.session.get('username', default=None)
    return render(request,'regist/notifications.html',locals())

@login_required
def contact(request):
    username = request.session.get('username', default=None)
    customerid = request.session.get('userid', default=None)
    contact_list = Contact.objects.filter(customer_id=customerid).order_by("-id")
    paginator = Paginator(contact_list, 6)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render(request,'regist/contact.html',locals())

def contact_add(request):

    Method = request.method
    if Method == 'POST':
        # 如果有post提交的动作，就将post中的数据赋值给uf，供该函数使用
        uf = ContactForm(request.POST)

        if uf.is_valid():
            name = uf.cleaned_data['name']
            cardid = uf.cleaned_data['cardid']
            telephone = uf.cleaned_data['telephone']
            weixin = uf.cleaned_data['weixin']
            age = uf.cleaned_data['age']
            sex = uf.cleaned_data['sex']
            print(sex)
            #description = uf.cleaned_data['description']
            customerid = request.session.get('userid', default=1)
            errors = []
            contactAdd = Contact.objects.create(name=name,cardid=cardid,telephone=telephone,weixin=weixin,age=age,sex=sex,customer_id=customerid,is_active=1)

            response = HttpResponseRedirect('/regist/contact/')
            return response
        else:
            errors=uf.errors
            return render(request, 'regist/contact.html', locals())
    else:
        uf = ContactForm()
    return render(request,'regist/contact.html',locals())

