from django import forms
from django.forms import ModelForm
from .models import Flor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FlorForm(ModelForm):
    nombre = forms.CharField(min_length=3, max_length=150)
    valor = forms.IntegerField(min_value=890, max_value=250000)
    stock = forms.IntegerField(max_value=10000)

    class Meta:
        model = Flor
        fields = ['imagen','nombre', 'valor','tipo','descripcion','estado','stock']

class CustomUserForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['first_name','last_name','email','username','password1','password2']
