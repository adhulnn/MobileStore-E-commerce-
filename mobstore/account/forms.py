from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class RegForm(UserCreationForm):
    class Meta:
        model=CustomUser
        fields=["first_name","last_name","email","phone","address","image","usertype","username","password1","password2"]
        widgets = {
            
            'first_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your first name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your last name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control','placeholder':'Enter your email id'}),
            'phone': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your phone number'}),
            'address': forms.TextInput(attrs={'class': 'form-control','placeholder':'Enter your address'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'usertype': forms.Select(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control','placeholder':'Pick a Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
            
        }

class LogForm(forms.Form):
    username=forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class":"form-control","placeholder":"Enter your username Here"}))
    password=forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter your Password Here"}))