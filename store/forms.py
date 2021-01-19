from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordChangeForm,
                                       UserChangeForm, UserCreationForm)
from django.contrib.auth.models import User
from django.db.models.fields import IntegerField
from django.forms.models import ModelForm
from .models import *


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
      model = User
      fields = ('username', 'first_name', 'last_name',
              'email', 'password1', 'password2')

'''


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
      model = Customer
      fields = ['user', 'username', 'name', 'email', 'password']

'''
class UpdateUserForm(UserChangeForm):
    password = None

    class Meta:
      model = User
      fields = ['username', 'first_name', 'last_name', 'email']


class EditUserProfileForm(UserChangeForm):
    password = None
    username = forms.CharField(disabled=True)
    date_joined = forms.DateTimeField(disabled=True)
    last_login = forms.DateTimeField(disabled=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'date_joined', 'last_login']


class CheckoutForm(forms.ModelForm):
    address = forms.CharField(max_length=200)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    pincode = forms.IntegerField()

    class Meta:
        model = ShippingAddress
        fields = ['address', 'city', 'state', 'pincode']

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'

class ProductUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'
