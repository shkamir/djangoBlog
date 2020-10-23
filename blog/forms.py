from django.forms import ModelForm
from django import forms
from .models import Contact


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
        
