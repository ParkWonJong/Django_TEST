from django import forms
from app.models import UserProfileInfo
from django.contrib.auth.models import User
from .models import UploadFileModel


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())


class Meta():
    model = User
    fields = ('username', 'password', 'email')


class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UploadFileForm(forms.Form):
    name = forms.CharField(max_length = 15)
    # files = forms.FileField()
    files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
