from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from shopsys.apps.plan.forms import  PlanForm,PlaneForm,TrainForm,HotelForm,Plan_ContactForm
from django.http import HttpRequest,HttpResponse,HttpResponseRedirect
from shopsys.apps.plan.models import Plan,Plane_plan
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from shopsys.apps.regist.models import Contact


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
    uf=Plan_ContactForm()
    Plan_ContactForm.fields['contact'].choices = get_contact(request)
    return render (request,'plan/plan_detail.html',locals())

def get_contact(request):
    r = [('', '----')]
    customerid = request.session.get('userid', default=None)
    contact_list = Contact.objects.filter(customer_id=customerid)
    for obj in contact_list:
       r = r + [(obj.id, obj.name)]
    return r

#飞机列表类
class Cart_plane(object):
    def __init__(self, *args, **kwargs):
        self.items = []

    def add_plan(self,product):
        self.total_price += product.price
        for item in self.items:
              if item.product.id == product.id:
                  item.quantity += 1
        return  self.items.append(Plane_plan(product=product,unit_price=product.price,quantity=1))

#显示购物车
def view_cartplan(request):
    cart = request.session.get("cart",None)
    if not cart:
        cart = Cart_plane()
        request.session["cart"] = cart
    return render(request,'plan/plan_detail.html',locals())

#添加到购物车
def add_to_cart(request,id):
    product = Plane_plan.objects.get(id = id)
    cart = request.session.get("cart",None)
    if not cart:
        cart = Cart()
        request.session["cart"] = cart
        cart.add_product(product)
        request.session['cart'] = cart
    return view_cart(request)

#清空购物车
def clean_cart(request):
    request.session["cart"] = Cart()
    return view_cart(request)