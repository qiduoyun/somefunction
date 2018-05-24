#conding:utf-8
from django import forms

class UserRegister(forms.Form):
    user_name=forms.CharField(label="注册用户名",max_length=100)
    user_password=forms.CharField(label="设置密码",widget=forms.PasswordInput())
    user_password_sure=forms.CharField(label="确认密码",widget=forms.PasswordInput())

class UserLogin(forms.Form):
    user_name=forms.CharField(label="用户名",max_length=100)
    user_password=forms.CharField(label="密码",widget=forms.PasswordInput())

class UserFileForm(forms.Form):
    file_name=forms.CharField(max_length=100)
    file_upload=forms.FileField()
