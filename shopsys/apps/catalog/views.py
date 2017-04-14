from django.shortcuts import render,get_object_or_404
from .models import Category,Product

# Create your views here.

def index(request):
    page_title='产品分类目录'
    username= request.session.get('username',default=None)
    return render(request,'catalog/index.html',locals())

def show_category(request,category_slug):
    c = get_object_or_404(Category,slug=category_slug)
    products=c.product_set.all()
    page_title=c.name
    meta_keywords=c.meta_keywords
    meta_description=c.meta_description
    return render(request,'catalog/category.html',locals())

def show_product(request,product_slug):
    p = get_object_or_404(Product,slug=product_slug)
    categories=p.categories.filter(is_active=True)
    page_title=p.name
    meta_keywords=p.meta_keywords
    meta_description=p.meta_description
    return render(request,'catalog/products.html',locals())
