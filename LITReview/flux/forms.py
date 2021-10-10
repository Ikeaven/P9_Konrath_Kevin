from django import forms
from .models import Ticket, UserFollows

# class CritiqueRequestForm(forms.Form):
#     title = forms.CharField(label='Titre', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control my-3'}))
#     description = forms.CharField(label='Descritpion', max_length=2048, widget=forms.Textarea(attrs={'class': 'form-control my-3'}))
#     image = forms.ImageField(label='Image', required=False, widget=forms.FileInput(attrs={'class': 'm-4'}))

#     def __init__(self, *args, **kwargs):
#         super(CritiqueRequestForm, self).__init__(*args, **kwargs)
#         for visible in self.visible_fields():
#             visible.field.widget.attrs['class'] = 'form-control'

class CritiqueRequestForm(forms.ModelForm):

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']

    def __init__(self, *args, **kwargs):
            super(CritiqueRequestForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'


RATING_CHOICES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]


class ReviewForm(forms.Form):
    headline = forms.CharField(label='Titre', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control my-3'}))
    rating = forms.ChoiceField(label='Notes', choices=RATING_CHOICES, widget=forms.RadioSelect(attrs={'class':'form-check form-check-inline'}))
    body = forms.CharField(label='Commentaire', max_length=8192, widget=forms.Textarea(attrs={'class': 'form-control my-3'}))


class AbonnementsForm(forms.Form):
    name = forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput(attrs={'class': 'form-control my-3'}))