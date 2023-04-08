from django.urls import path
from .views import *
# from django.conf import settings
# from django.conf.urls.static import static

urlpatterns=[
    path('strh/',S_Home.as_view(),name="sh"),
    path('addm/',AddMob.as_view(),name="ad"),
    path('prof/',ProView.as_view(),name="pro"),
    path('edm/<int:pk>',Edit_mob.as_view(),name="em"),
    path('ddm/<int:pk>',Delete_mob.as_view(),name="dm"),
    path('searchh/', search_resultss, name='search_resultss'),
    # path('soders/<int:mobile_id>/orders/', sorders, name='sords'),
    path('orders/<int:order_id>/', order_detail, name='order_detail'),
    path('mobiles-and-orders/', mobiles_and_orders, name='mobiles_and_orders'),



] 