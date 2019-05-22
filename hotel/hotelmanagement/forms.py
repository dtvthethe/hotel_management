from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions

from .models import ProductType, RoomType, Client, Config, PaymentType, Product, Room, Person


class ProductTypeForm(forms.ModelForm):
    class Meta:
        model = ProductType
        fields = ['name']


class RoomTypeForm(forms.ModelForm):
    class Meta:
        model = RoomType
        fields = ['name']


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name']


class ConfigForm(forms.ModelForm):
    class Meta:
        model = Config
        fields = ['name', 'data_value']


class PaymentTypeForm(forms.ModelForm):
    class Meta:
        model = PaymentType
        fields = ['name']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'product_type']


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'price', 'capacity', 'room_status', 'room_type']


class PersonForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Person
        fields = (
            'username', 'is_active', 'is_staff', 'is_superuser', 'first_name', 'last_name', 'email', 'password',
            'avatar'
        )


class PersonEditForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = (
            'username', 'is_active', 'is_staff', 'is_superuser', 'first_name', 'last_name', 'email', 'avatar'
        )


class PersonChangePasswordForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password1 = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['password']


class LoginForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    username.widget.attrs.update(
        {'class': 'form-control', "id": "inputEmail", "placeholder": "Password", "required": "required",
         "autofocus": "autofocus"})

    password = forms.CharField(widget=forms.PasswordInput)
    password.widget.attrs.update(
        {'class': 'form-control', "id": "inputPassword", "placeholder": "Username", "required": "required"})

    class Meta:
        model = User
        fields = ['username', 'password']
