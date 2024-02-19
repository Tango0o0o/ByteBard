from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

def is_authenticated_func(user): # this is to check whether the user is already logged in
    return user.is_authenticated

def home(req):
    return render(req, "base.html")