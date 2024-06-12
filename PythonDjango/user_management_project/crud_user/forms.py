from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import User

class UserSignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'date_of_birth']

class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'date_of_birth']

class PasswordChangeCustomForm(PasswordChangeForm):
    pass