from typing import Any
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    #adding fields
    first_name = forms.CharField(max_length=30, label="First name")
    last_name = forms.CharField(max_length=30, label="Last name")

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields['password2'].required = False # Password2 isn't needed to make the user (no password confirmation)
        # labels for fields i added
        self.fields["first_name"].label = "First name"
        self.fields["last_name"].label = "Last name"

        for field in self.fields:
            self.fields[field].widget.attrs.update({"class" : "form-input", "id" : f"{field}", "required" : True}) # adding the class "form-input" to every field, to allow CSS changes to be made. Also added placeholder text for the input box
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', "first_name", "last_name"] # Adding the fields
