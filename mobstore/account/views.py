from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView,CreateView,FormView,View
from .forms import *
from .models import CustomUser
from  django.contrib.auth import authenticate,login,logout
# Create your views here.
class Reg(CreateView):
    template_name="reg.html"
    form_class=RegForm
    model=CustomUser
    success_url=reverse_lazy("h")

class Hom(TemplateView):
    template_name="home.html"

class Log(FormView):
    template_name="log.html"
    form_class=LogForm

    def post(self,request,*args,**kwargs):
        f=LogForm(data=request.POST)
        if f.is_valid():
            u=f.cleaned_data.get("username")
            p=f.cleaned_data.get("password")
            user=authenticate(request,username=u,password=p)
            if user:
                if user.usertype == 'Customer':
                    login(request, user)
                    return redirect('chm')
                elif user.usertype == 'Store':
                    login(request, user)
                    return redirect('sh')
            else:
                return redirect("login")

class LogOut_(View):
     def get(self,request):
        logout(request)
        # messages.error(request,"user logged out")
        return redirect("login")