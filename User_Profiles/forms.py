from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class User_Custom_Form(UserCreationForm):




    phone= forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address_1= forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address_2= forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    country= forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control'}))
    city= forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control'}))
    state= forms.CharField(max_length=60, widget=forms.TextInput(attrs={'class': 'form-control'}))
    zip_code= forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ["phone", "address_1", "address_2", "country", "city", "state", "zip_code"]