# encoding:utf-8
from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(CustomerForm, self).clean()
        value = cleaned_data.get("name")
        try:
            Customer.objects.get(name=value)
            self.errors["name"] = self.error_class(["%s的出版社信息已存在" % value])
        except Customer.DoesNotExist:
            pass
        return cleaned_data

    class Meta:
        model = Customer
        exclude = {"id", }
