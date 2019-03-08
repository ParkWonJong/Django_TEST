from django.shortcuts import render
from app.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate, login,logout
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, UploadFileForm
from django.template import RequestContext
from .models import Playlist

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



def Upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES["document"]
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

    return render(request, 'upload.html',context)

def test(request):
    return render(request,'test.html')

def NCS_playlist(request):
    playlists = Playlist.objects.all().order_by('date')
    return render(request, 'playlist.html', {'playlists':playlists})

def playlist_detail(request,slug):
    playlist = Playlist.objects.get(slug=slug)
    return render(request, "playlist_detail.html", {'playlist':playlist})