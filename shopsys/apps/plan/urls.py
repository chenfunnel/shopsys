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
from shopsys.apps.plan import  views


urlpatterns = [
    url(r'^plan/$', views.plan,name='plan'),
    url(r'^planlist/$', views.planlist,name='planlist'),
    url(r'^plandetail/$', views.plandetail,name='plandetail'),
    url(r'^contactlist/$',views.contactlist.as_view(),name='contactlist'),
    url(r'^contactdetail/(?P<pk>[0-9]+)$',views.contact_detail,name='contactdetail'),
    url(r'^planelist/$', views.PlaneList.as_view(),name='planelist'),
    url(r'^trainlist/$', views.TrainList.as_view(),name='trainlist'),
    url(r'^hotellist/$', views.HotelList.as_view(),name='hotellist'),
    url(r'^plancontact/$', views.contactview.as_view(),name='plancontact'),
]