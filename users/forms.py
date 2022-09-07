from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password1',
            'password2'
        ]

        # widgets = {
        #     "first_name": forms.TextInput(attrs={
        #         "placeholder": "firstname"
        #     }),
        #     "last_name": forms.TextInput(attrs={
        #         "placeholder": "lastname"
        #     }),
        #     "username": forms.TextInput(attrs={
        #         "placeholder": "username"
        #     }),
        #     "email": forms.TextInput(attrs={
        #         "placeholder": "email"
        #     }),
        #     "password1": forms.TextInput(attrs={
        #         "placeholder": "password"
        #     }),
        #     "password2": forms.TextInput(attrs={
        #         "placeholder": "confirm password"
        #     }),
        # }


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            "username",
            "email",
        ]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
