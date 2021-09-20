from django import forms
from .models import Ticket

class CritiqueRequestForm(forms.Form):
    title = forms.CharField(label='Titre', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control my-3'}))
    description = forms.CharField(label='Descritpion', max_length=2048, widget=forms.Textarea(attrs={'class': 'form-control my-3'}))
    image = forms.ImageField(label='Image', required=False)

# class CritiqueRequestForm(forms.ModelForm):

#     class Meta:
#         model = Ticket
#         fields = ['title', 'description', 'image']