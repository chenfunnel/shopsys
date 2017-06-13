from django.contrib import admin
from .models import Plane,Train,Hotel

# Register your models here.


@admin.register(Plane)
class PlaneAdmin(admin.ModelAdmin):
    list_display = ('name','companyname','planetype','fromcity','tocity','start_at','arrive_at','fromstation','tostation','classtype','price','description')
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['id']
    search_fields = ['name','companyname','fromcity','tocity',]
    exclude = ('create_at','update_at')

@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    list_display = ('name','traintype','fromstation','tostation','start_at','arrive_at','classtype','price','description')
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['id']
    search_fields = ['name','companyname','fromstation','tostation',]
    exclude = ('create_at','update_at')

@admin.register(Hotel)
class TotelAdmin(admin.ModelAdmin):
    list_display = ('name','city','hoteltype','address','coordinate','classtype','price','description')
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['id']
    search_fields = ['name','city','hoteltype','address',]
    exclude = ('create_at','update_at')