from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()

    password1 = forms.CharField(
        label= ("Password"),
        strip=False,
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label= ("Confirm Password"),
        widget=forms.PasswordInput,
        strip=False,
    )

    class Meta:
         model = User
         fields = ['username', 'email', 'password1', 'password2']


class EditUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['email']


class EditProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ['image', 'first_name', 'last_name', 'country']