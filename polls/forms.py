from django.forms import ModelForm,widgets
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *
from django import forms
from datetime import date


class CreateUserForm(UserCreationForm):
    class Meta:
       model = User
       fields = ['username', 'email', 'password1', 'password2']


class DateInput(forms.DateInput):
    input_type = 'date'


class VacationForm(ModelForm):
    class Meta:
        model = Vacation
        fields = '__all__'
        widgets = {
            'date_from': DateInput(),
            'date_to': DateInput(),
        }
        exclude = ('employee',)
