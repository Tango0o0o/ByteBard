from django.shortcuts import render, HttpResponse
from django.template import loader
# Create your views here.

def home(req):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def login(req):
    return HttpResponse("lOGIN")

def register(req):
    template = loader.get_template('registration/Register.html')
    return HttpResponse(template.render())