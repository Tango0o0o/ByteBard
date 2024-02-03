from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import CreateUserForm
# Create your views here.

def home(req):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def login(req):
    if req.user:
        print("Yay")
    return HttpResponse("lOGIN")

def register(req):
    if req.method == "POST":
        form = CreateUserForm(req.POST)
        
        if form.is_valid():
            user = form.save()
            login(req)
            return redirect(reverse("home"))
        else:
            return render(req, 'registration/Register.html', {"form":form})

    form = CreateUserForm()
    return render(req, 'registration/Register.html', {"form":form})