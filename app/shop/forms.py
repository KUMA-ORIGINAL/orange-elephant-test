from django import forms
from django.contrib.auth.models import User

from shop.models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
