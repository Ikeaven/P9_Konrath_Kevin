from django.forms.utils import ErrorList
from django import forms
# from django.contrib.auth.models import User


class InscriptionForm(forms.Form):
    username = forms.CharField(
        label="Nom d'utilisateur", max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control my-3'}))
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput(attrs={'class': 'form-control my-3'}))
    verify_password = forms.CharField(label='Verifier le mot de passe', widget=forms.PasswordInput(
        attrs={'class': 'form-control my-3'}))


class DivErrorList(ErrorList):

    def __str__(self):
        return self.as_divs()

    def as_divs(self):
        if not self:
            return ''
        return '<div class="errorlist">%s</div>' % ''.join(
            ['<div class="error text-danger">%s</div>' % e for e in self])
