from django.urls import path
from .views import *

urlpatterns=[
    path('chm/',C_home.as_view(),name="chm"),
    path('md/<int:pk>',MobDetail.as_view(),name="md"),
    path('search/', search_results, name='search_results'),
    path('profc/',ProView_cust.as_view(),name="prov"),
    path('cart/',cart,name="cart"),
    # path('ords/',Orders.as_view(),name="odrs"),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='addcrt'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='removecrt'),
    path('update-cart/<int:item_id>/', update_cart, name='upcrt'),
    path('checkout/', checkout, name='checkout'),
    path('order_confirmation/', order_confirmation, name='order_confirmation'),
    path('orders/', my_orders, name='myords'),
    path('orders/<int:order_id>/delete/', delete_order, name='delete_order'),
    path('review/<int:mobile_id>', review_product, name='review_product'),

]