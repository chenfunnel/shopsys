from django.contrib import admin
from .models import Category,Product
from .forms import ProductAdminForm

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ('name','price','old_price','create_at','update_at',)
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-create_at']
    search_fields = ['name','description','meta_keywords','meta_description',]
    exclude = ('create_at','update_at')
    prepopulated_fields = {'slug':('name',)}

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'create_at', 'update_at',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['-create_at']
    search_fields = ['name', 'description', 'meta_keywords', 'meta_description', ]
    exclude = ('create_at', 'update_at')
    prepopulated_fields = {'slug': ('name',)}


# Register your models here.
