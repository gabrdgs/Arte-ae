# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User

class UserModelForm(forms.ModelForm):
  User._meta.get_field('email').blank = False
  class Meta:
    model = User
    fields = ['username','first_name','last_name','email','password']
    widgets = {
      'username': forms.TextInput(attrs={'class': 'form-control'}),
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),      
      'password': forms.PasswordInput(attrs={'class': 'form-control'})
    }