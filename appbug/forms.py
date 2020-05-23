from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Bug


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)


class CustomUserCreationForm(UserCreationForm):
    display_name = forms.CharField(max_length=50)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'display_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class AddBugForm(forms.ModelForm):
    class Meta:
        model = Bug
        fields = [
            'title',
            'description'
        ]
