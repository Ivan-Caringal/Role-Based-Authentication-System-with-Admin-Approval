from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.

def index(response):
    return render(response,"index.html")

def landing(response):
    return render(response,"landingpage.html")