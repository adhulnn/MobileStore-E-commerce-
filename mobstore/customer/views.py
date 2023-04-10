from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView,FormView,CreateView,UpdateView
from store.models import Mobile
from .models import Cart,Order,OrderItem
from django.db.models import Q
from django.db.models import Sum
from django.db import transaction
from .forms import OrderForm,ReviewForm
from store.models import Review
from django.contrib import messages
from django.db.models import Avg





# Create your views here.

class C_home(TemplateView):
    template_name="CustHome.html"
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["data"]=Mobile.objects.all().order_by('-datetime')
        return context
    
class MobDetail(TemplateView):
    template_name="mobdetails.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk') 
        mobile = get_object_or_404(Mobile, pk=pk)  
        context["mobile"] = mobile 
        reviews = Review.objects.filter(mobile=mobile).order_by('-createdat')
        context["reviews"] = reviews

        avg_rating = Review.objects.filter(mobile=mobile).aggregate(Avg('rating'))['rating__avg']
        context["avg_rating"] = round(avg_rating, 1) if avg_rating else None

        print(reviews) 
        return context

def search_results(request):
    query = request.GET.get('q')
    if query:
        results = Mobile.objects.filter(
            Q(brand__icontains=query) | 
            Q(model__icontains=query) |
            Q(specs__icontains=query)
        )
    else:
        results = Mobile.objects.all()
    return render(request, 'search_results.html', {'results': results})

class ProView_cust(TemplateView):
    template_name="profile.html"

class Kart(TemplateView):
    template_name="cart.html"




def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    context = {
        'cart_items': cart_items,
    }
    return render(request, 'cart.html', context)


def add_to_cart(request, product_id):
    product = get_object_or_404(Mobile, pk=product_id)
    cart_product, created = Cart.objects.get_or_create(
        user=request.user,
        product=product
    )
    if not created:
        cart_product.quantity += 1
        cart_product.save()
    return redirect('cart')

def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(Cart, pk=item_id)
    cart_item.delete()
    return redirect('cart')

def update_cart(request, item_id):
    cart_item = get_object_or_404(Cart, pk=item_id)
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
    return redirect('cart')

# checkout

@transaction.atomic
def checkout(request):
   
    cart_items = Cart.objects.filter(user=request.user)
    

   
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart_items:
                order.mobile.add(item.product)
                # order.quantity.update(item.quantity)
                

            
            cart_items.delete()

            return redirect('order_confirmation')
    else:
        form = OrderForm()

    context = {
        'form': form
    }

    return render(request, 'checkout.html', context)

# order confirmation

def order_confirmation(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'orders': orders
    }
    return render(request, 'order_confirmation.html', context)

# view order section

def my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    cform = ReviewForm(request.GET)
    context = {
        'orders': orders,
        'cform': cform,
    }
    return render(request, 'myorders.html', context)





# delete order

def delete_order(request, order_id):
    order = Order.objects.get(id=order_id)
    order_items = OrderItem.objects.filter(order=order)
    
    for order_item in order_items:
        order_item.delete()

    order.delete()
    return redirect('myords')


# 08-04-2023

def review_product(request, mobile_id):
    mobile = get_object_or_404(Mobile, id=mobile_id) 
   
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        print(form)
        if form.is_valid():
            review = form.save(commit=False)
            review.mobile = mobile
            
            review.user = request.user
            review.save()
            return redirect('myords')
    else:
        form = ReviewForm()
    context = {
        'mobile': mobile,
        'form': form,
       
    }
    return render(request, 'myorders.html', context)


