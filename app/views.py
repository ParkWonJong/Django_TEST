from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    template_name = "home.html"

def index(request):
    return render(request, "index.html")
