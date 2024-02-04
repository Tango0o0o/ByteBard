from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .forms import CreateUserForm, LoginForm
# Create your views here.

def is_authenticated(user):
    return user.is_authenticated
    

def home(req):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def loginview(req):
    if is_authenticated(req.user) == True:
        return redirect(reverse("home"))

    if req.method == "POST":
        form = LoginForm(req.POST)
        username = req.POST["username"]
        password = req.POST["password"]
        user = authenticate(req=req, username=username, password=password)
        if user is not None:
            login(request=req,user=user)
            return redirect(reverse("home"))

    form = LoginForm()
    return render(req, 'authentication/login.html', {"form":form})

def register(req):
    if is_authenticated(req.user) == True:
        return redirect(reverse("home"))
    
    if req.method == "POST":
        form = CreateUserForm(req.POST)
        
        if form.is_valid():
            user = form.save()
            login(req, user=user)
            return redirect(reverse("home"))
        else:
            return render(req, 'registration/Register.html', {"form":form})

    form = CreateUserForm()
    return render(req, 'registration/Register.html', {"form":form})

def logoutview(req):
    logout(request=req)
    return redirect(reverse("home"))