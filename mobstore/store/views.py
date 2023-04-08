from django.shortcuts import render,redirect
from django.views.generic import TemplateView,FormView,CreateView,UpdateView,DeleteView
from .forms import *
from django.urls import reverse_lazy
from .models import *
from django.db.models import Q
from customer.models import Order


# Create your views here.
class S_Home(TemplateView):
    template_name="storeHome.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Mobile.objects.filter(user=self.request.user).order_by('-datetime')
        return context
    


class AddMob(CreateView):
    form_class=MobForm
    template_name="addmob.html"
    model=Mobile
    success_url=reverse_lazy("sh")
    def form_valid(self, form):
        form.instance.user=self.request.user
        self.object=form.save()
        return super().form_valid(form)

class Edit_mob(UpdateView):
    form_class=MobForm
    template_name="editmob.html"
    model=Mobile
    success_url=reverse_lazy("sh")
    pk_url_kwargs="pk"

class Delete_mob(DeleteView):
    model=Mobile
    template_name="deletemobile.html"
    success_url=reverse_lazy("sh")

#profile

class ProView(TemplateView):
    template_name="storeprofile.html"

def search_resultss(request):
    query = request.GET.get('q')
    if query:
        results = Mobile.objects.filter(
            Q(brand__icontains=query) | 
            Q(model__icontains=query) |
            Q(specs__icontains=query)
        )
    else:
        results = Mobile.objects.all()
    return render(request, 'search_resultss.html', {'results': results})

def sorders(request, mobile_id):
    mobile = Mobile.objects.get(id=mobile_id)
    orders = Order.objects.filter(mobile=mobile, user=request.user)
    context = {
        'mobile': mobile,
        'orders': orders
    }
    return render(request, 'store/orders.html', context)

def order_detail(request, order_id):
    order = Order.objects.get(id=order_id)
    mobiles = order.mobile.all()
    context = {
        'order': order,
        'mobiles': mobiles,
    }
    return render(request, 'order_detail.html', context)

def mobiles_and_orders(request):
    # Get all mobiles that are associated with the current user
    mobiles = Mobile.objects.filter(user=request.user)
    # Get all orders that have mobiles associated with them
    orders = Order.objects.prefetch_related('mobile').all()
    context = {
        'mobiles': mobiles,
        'orders': orders,
    }
    return render(request, 'mobiles_and_orders.html', context)
    
