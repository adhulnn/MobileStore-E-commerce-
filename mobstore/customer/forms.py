from django import forms
from .models import Order
from store.models import Review

class OrderForm(forms.ModelForm):
    payment_method = forms.ChoiceField(choices=[('', '-- Select Payment Method --'), ('Credit_Card', 'Credit Card'), ('PayTm', 'PayTm'), ('PhonePe', 'PhonePe'), ('Google Pay', 'Google Pay')])
    
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'city', 'state', 'zip_code', 'payment_method']

class ReviewForm(forms.ModelForm):
    rating = forms.ChoiceField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')), widget=forms.RadioSelect)

    class Meta:
        model = Review
        fields = ['rating', 'comment']
        labels = {
            'rating': 'Rating (out of 5)',
            'comment': 'Comment (optional)',
        }