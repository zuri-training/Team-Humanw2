
from  .models import Comment, Design
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms
class usersignupform(ModelForm):
        class Meta:
            model=User
            fields=['email', 'username', 'password']
            widgets={'password': forms.PasswordInput()}

class designForm(ModelForm):
    class Meta:
        model=Design
        fields=['file', 'name', 'description']
        

class commentForm(ModelForm):
    class Meta:
        model=Comment
        fields=['comment']