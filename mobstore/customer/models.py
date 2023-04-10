from django.db import models
from account.models import CustomUser
from store.models import Mobile
from django.urls import reverse

class Cart(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    date_added = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('cart')

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,related_name="cartitem_set")
    quantity = models.PositiveIntegerField(default=1)
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE)

    def get_total(self):
        return self.quantity * self.mobile.price

    def __str__(self):
        return f'{self.quantity} of {self.mobile.name} in cart'


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    mobile = models.ManyToManyField(Mobile, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    payment_method = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name="orderitem_set")
    mobile = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.quantity} of {self.mobile.name} in order {self.order.id}'