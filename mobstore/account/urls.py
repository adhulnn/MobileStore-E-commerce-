from django.urls import path
from .views import *


urlpatterns=[
    path('reg/',Reg.as_view(),name="register"),
    path('log/',Log.as_view(),name="login"),
    path('logout/',LogOut_.as_view(),name="logout"),
]