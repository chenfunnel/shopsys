# encoding:utf-8
from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(CustomerForm, self).clean()
        value = cleaned_data.get("name")
        try:
            Customer.objects.get(name=value)
            self.errors["name"] = self.error_class(["%sx客户已存在" % value])
        except Customer.DoesNotExist:
            pass
        return cleaned_data

    class Meta:
        model = Customer
        exclude = {"id", }

# Create your views here.
#用户注册表单
class UserForm(forms.Form):
    name  = forms.CharField(label="姓  名",max_length=50)
    username  = forms.CharField(label='用 户 名',max_length=50)
    password1 = forms.CharField(label='密   码',widget=forms.PasswordInput())
    password2 = forms.CharField(label='确认密码',widget=forms.PasswordInput())

#用户登录表单
class LoginForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=50)
    password = forms.CharField(label='密  码',widget=forms.PasswordInput())

