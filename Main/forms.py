from typing import Any
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User

class LoginForm(forms.Form):

    username = forms.CharField(label="Username", required=True)
    password = forms.CharField(label="Password", required=True, widget=(forms.PasswordInput()))

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
    
        self.fields["password"].widget.attrs.update({"type" : "password"})
        self.fields["username"].widget.attrs.update({"type" : "text"})

        for field in self.fields:
            self.fields[field].widget.attrs.update(
               {    
                "class" : "form-input",
                "placeholder" : "",
                "id" : f"{field[3]}",
                "required" : True
                }
            ) # adding the class "form-input" to every field, to allow CSS changes to be made. Also added placeholder text for the input box

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

        self.fields["email"].error_messages={"invalid" : "Enter a valid email, such as name@example.com"} # changing error message
        
        self.fields["first_name"].widget.attrs.update(
                {
                "type" : "text", 
                "autofocus" : True, 
                "pattern" : "[A-Za-z]+"# setting it to only allow lwtter upper and lower case
                }
            ) 
        
        self.fields["last_name"].widget.attrs.update(
                {
                "type" : "text", 
                "pattern" : "[A-Za-z]+"
                }
            )
        
        self.fields["password1"].widget.attrs.update(
            {
                "minlength" : "8"
                }
            ) # min password length of 8

        for field in self.fields:
            print(field)
            input_id = "'id" + "_"+ field + "'" # Setting the ids to be passed to the live/late validation functions (just saves rewriting code) puts it in the form 'id_fieldname'
            label_id = "'input-label" + "-"+ field + "'"

            self.fields[field].widget.attrs.update(
                    {
                    "class" : "form-input",
                    "placeholder" : "",
                    "onkeydown" : f"reward_early({input_id}, {label_id})",
                    "required" : True,
                    "minlength" : "1"
                    }
                ) # adding the class "form-input" to every field, to allow CSS changes to be made. Also added placeholder text for the input box

        

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', "first_name", "last_name"] # Adding the fields
