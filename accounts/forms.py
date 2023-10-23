from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   "placeholder": "Enter Your Email"}
            ),
            label = ""
    )

    first_name = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   "placeholder": "Enter Your First Name"}
            ),
            label = ""
    )

    last_name = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   "placeholder": "Enter Your Last Name"}
            ),
            label = ""
    )

    class Meta:
        model = User
        fields =('username','first_name','last_name','email','password1','password2')