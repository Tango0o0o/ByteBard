from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from .forms import CreateUserForm, LoginForm, UpdateUserForm
# Views to do with the users account

def is_authenticated_func(user): # this is to check whether the user is already logged in
    return user.is_authenticated

def loginview(req):
    form = LoginForm()

    
    not_found = False

    if is_authenticated_func(req.user) == True: # if you are logged in, you can't access this page
        return redirect(reverse("home"))

    if req.method == "POST":
        # getting credentials and veriying them, then taking action
        form = LoginForm(req.POST)

        username = req.POST["username"]
        password = req.POST["password"]
        user = authenticate(req=req, username=username, password=password) # verifies that the credentials are valid
        
        if user is not None: # log the user in if there is one, and send to home page
            login(request=req,user=user) 
            return redirect(reverse("home"))
        
        else: # If there is no user, make not_found true to trigger error message ni the template 
            not_found = True
    form.password = ""
    return render(req, 'authentication/login.html', {"form":form, "not_found":not_found})

def register(req):
    if is_authenticated_func(req.user) == True: # if you are logged in, you can't access this page
        return redirect(reverse("home"))
    
    if req.method == "POST":
        form = CreateUserForm(req.POST)
        
        if form.is_valid(): # validating form
            user = form.save() # creating user
            login(req, user=user) # logging user in
            return redirect(reverse("home")) # redirect to homepage
        
        else:
            return render(req, 'registration/Register.html', {"form":form}) # return form with the errors
    
    form = CreateUserForm()
    return render(req, 'registration/Register.html', {"form":form})

def logoutview(req):
    logout(request=req)
    return redirect(reverse("home"))

def profile(req):
    # populating the Updateform with the users data (password done in forms.py)
    user = req.user
    form = UpdateUserForm() 
    form['first_name'].initial = user.first_name
    form['last_name'].initial = user.last_name
    form['username'].initial = user.username
    form['email'].initial = user.email


    return render(req, 'profile/profile.html', {"form":form})