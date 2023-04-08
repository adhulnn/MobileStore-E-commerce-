from django import forms
from .models import *


class MobForm(forms.ModelForm):
    class Meta:
        model=Mobile
        exclude=["user"]
        widgets={
            "brand":forms.TextInput(attrs={"class":"form-control"}),
            "model":forms.TextInput(attrs={"class":"form-control"}),
            "price":forms.NumberInput(attrs={"class":"form-control"}),
            "specs":forms.TextInput(attrs={"class":"form-control"}),
            
        }

class ProfileForm(forms.ModelForm):
    pass
