from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    phone=models.IntegerField(null=True)
    address=models.CharField(null=True,max_length=500)
    image=models.ImageField(upload_to="profile_pic",null=True)
    options=(
        ("Store","Store"),
        ("Customer","Customer"),
    )
    usertype=models.CharField(max_length=100,choices=options,default="Customer")