from django.forms import ModelForm
from django import forms
from .models import Contact
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm 


class ContactForm(ModelForm):
    name = forms.CharField(
        label="name",
        label_suffix="",
        widget=forms.TextInput(
            attrs={"class":"form-control", "placeholder": "Type in Your Name"},
        ),
        required=True,
    )
    email = forms.EmailField(
        label="email",
        label_suffix="",
        widget=forms.EmailInput(
            attrs={"class":"form-control", "placeholder": "Enter Your Valid Email Address"}
        ),
        required=True,
    )
    message = forms.CharField(
        label="email",
        label_suffix="",
        widget=forms.Textarea(
            attrs={"class":"form-control", "placeholder": "Enter Your Message"}
        ),
        required=True,
    )
    file = forms.FileField(
        label="file",
        label_suffix="",
        widget=forms.FileInput(
            attrs={"class":"form-control-file"}
        ),
        required=False,
    )
    
    
    class Meta:
        model = Contact
        fields = "__all__"
        
class RegisterForm(UserCreationForm):
    first_name = forms.CharField(
        label = "Full Name",
        label_suffix="",
        widget = forms.TextInput(attrs={"class":"form-control"})
        )
    username = forms.CharField(
        label = "Username",
        label_suffix="",
        widget = forms.TextInput(attrs={"class":"form-control"})
        )
    email = forms.EmailField(
        label = "Email",
        label_suffix="",
        widget = forms.EmailInput(attrs={"class":"form-control"})
        )
    password1 = forms.CharField(
        label_suffix="",
        label="Password",
        widget = forms.PasswordInput(attrs={"class":"form-control"})
        )
    password2 = forms.CharField(
        label_suffix="",
        label="Confirm your password",
        widget = forms.PasswordInput(attrs={"class":"form-control"})
        )
    class Meta:
        model = User
        fields = (
            "first_name",
            "username",
            "email",
            "password1",
            "password2",
            )
        help_texts = {
            "username": None,
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label = "Username",
        label_suffix="",
        widget = forms.TextInput(attrs={"class":"form-control"})
        )
    password = forms.CharField(
        label_suffix="",
        label="Password",
        widget = forms.PasswordInput(attrs={"class":"form-control"})
        )

    class Meta:
        model = User
        fields = (
            "username",
            "password",
            )