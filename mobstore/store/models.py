from django.db import models
# from django.contrib.auth.models import User
from account.models import CustomUser


class Mobile(models.Model):
    brand = models.CharField(max_length=100, null=True)
    model = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2, null=True)
    specs = models.TextField(null=True)
    photo = models.ImageField(upload_to='mobile_photos', null=True)
    datetime = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="m_user")


    def __str__(self):
        return f"{self.brand} {self.model}"
    
class Profile(models.Model):
    dob=models.DateField()
    options=(
        ("Male","Male"),
        ("Female","Female"),
        ("Others","Others")
    )
    gender=models.CharField(max_length=100,choices=options,default="Male")
    phone=models.IntegerField()
    email=models.CharField(max_length=100)
    store_name=models.CharField(max_length=100,null=True)
    address=models.CharField(max_length=100)
    profile_pic=models.ImageField(upload_to="profile_pictures",null=True)
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE,related_name="pro_user")


class Review(models.Model):
    comment=models.TextField(blank=True)
    createdat=models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')),default=1)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="R_user")
    mobile=models.ForeignKey(Mobile,on_delete=models.CASCADE,related_name="R_mobile")
