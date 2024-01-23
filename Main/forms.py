from typing import Any
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label="First name")
    last_name = forms.CharField(max_length=30, label="Last name")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["first_name"].label = "First name"
        self.fields["last_name"].label = "Last name"

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class" : "form-input", "placeholder" : f"{field.capitalize()}"})
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', "password2", "first_name", "last_name"]