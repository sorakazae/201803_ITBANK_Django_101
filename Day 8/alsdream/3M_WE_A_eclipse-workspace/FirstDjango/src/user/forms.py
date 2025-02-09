'''
Created on 2018. 3. 24.

@author: admin
'''
from django.forms.models import ModelForm
from django.contrib.auth.models import User
from django import forms

class signForm(ModelForm):
    class Meta:
        password = forms.CharField(widget = forms.PasswordInput)
        model = User
        widgets = {
            'password' : forms.PasswordInput(),
        }
        fields=['username', 'password', 'email']
        
class loginForm(ModelForm):
    class Meta:
        password = forms.CharField(widget = forms.PasswordInput)
        model = User
        widgets = {
            'password' : forms.PasswordInput(),
        }
        fields = ['username','password',]