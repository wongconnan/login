from django.shortcuts import render,render_to_response
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from online.models import User
# Create your views here. #自定义表单模型
class UserForm(forms.Form):
     username = forms.CharField(label = '用户名:',max_length = 100)
     password = forms.CharField(label = '密码:',widget=forms.PasswordInput())
     email = forms.EmailField(label = '电子邮件:')
def mysite5(request):
     if request.method == 'POST':
         uf = UserForm(request.POST)
         if uf.is_valid():
            #获取表单元素
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            #将表单写入数据库
            user = User()
            user.username = username
            user.password = password
            user.email = email
            user.save()
            #返回注册成功页面
            return render_to_response('successful.html',{'username':username})
     else:
         uf = UserForm()
     return render_to_response('mysite5.html',{'uf':uf})
