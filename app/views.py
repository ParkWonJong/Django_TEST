from django.shortcuts import render
from app.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import LoginForm
import ctypes

def messageBox(title, text, style):
	return ctypes.windll.user32.MessageBoxW(None, text, title, style)

def index(request):
    return render(request, "index.html")

def success(request):
    return render(request,"success.html")

def dust(request):
    return render(request, "dust.html")

def user_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    return render(request,'login.html')

            else:
                messageBox("Warning","ID or PASSWORD ERROR!", 0)
                return render(request, 'login.html')
        else:
            form = LoginForm()
    return render(request, 'login.html', {
        'form': form
    })


def user_logout(request):
   logout(request)
   return render(request, 'index.html')
