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


# class PersonForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'is_active', 'is_staff', 'is_superuser', 'first_name', 'last_name',
#                   'email']

    #
    # def save(self):
    #     password = self.cleaned_data.pop('password')
    #     u = super().save()
    #     u.set_password(password)
    #     u.save()

class PersonForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            'username', 'is_active', 'is_staff', 'is_superuser', 'first_name', 'last_name','email'
        )

    def save(self, commit=True):
        user = super(PersonForm, self).save(commit=False)
        passs = self.cleaned_data['password']
        user.set_password(passs)
        if commit:
            user.save()

        return user