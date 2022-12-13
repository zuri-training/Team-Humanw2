from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
class usersignupform(ModelForm):
        class Meta:
            model=User
            fields=['email', 'username', 'password']
            widgets={'password': forms.PasswordInput()}
