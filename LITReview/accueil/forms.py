from django import forms
from django.contrib.auth.models import User

class InscriptionForm(forms.Form):
    username = forms.CharField(label='Your name', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control my-3'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control my-3'}))
    verify_password = forms.CharField(label='Verifier le mot de passe', widget=forms.PasswordInput(attrs={'class': 'form-control my-3'}))
    class Media:
        js = ("password_check.js")
    # class Meta:
    #     model = User