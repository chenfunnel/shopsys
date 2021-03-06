"""URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import  url
from shopsys.apps.regist import  views


# urlpatterns=[
#     url(r'^$',views.index,{'template_name':'catalog/index.html'},'catalog_home'),
#     url(r'^category/(?P<category_slug>[-\w]+)/$',views.show_category,{'template_name':'catalog/category.html'},'catalog_category'),
#     url(r'^product/(?P<product_slug>[-\w]+)/$',views.show_product,{'template_name':'catalog/product.html'},'catalog_product'),
# ]

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'^regist/$', views.regist,name='regist'),
    url(r'^login/$', views.login,name='login'),
    url(r'^user/$', views.user,name='user'),
    url(r'^maps/$', views.maps,name='map'),
    url(r'^contact/$', views.contact,name='contact'),
    url(r'^contactadd/$',views.contact_add,name='contact_add'),
    url(r'^notification/$', views.notificaiton,name='notification'),
    url(r'^logout/$', views.logout_view,name='logout'),
]