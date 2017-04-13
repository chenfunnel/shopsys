from django.contrib import admin
from .models import Customer,Contact


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name','loginname','telephont','regist_at')
    list_display_links = ('name',)
    list_per_page = 50
    ordering = ['-regist_at']
    search_fields = ['name','telephont','loginname']
    exclude = ('regist_at','update_at')

