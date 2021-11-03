from django import forms
from .models import Review, Ticket


class CritiqueRequestForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']

    def __init__(self, *args, **kwargs):
        super(CritiqueRequestForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class ReviewRequestForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']

    def __init__(self, *args, **kwargs):
        super(ReviewRequestForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            if visible.name == 'rating':
                RATING_CHOICES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]
                visible.field = forms.ChoiceField(choices=RATING_CHOICES, widget=forms.RadioSelect(
                    attrs={'class': 'form-check form-check-inline'}))
            elif visible.name == 'headline':
                visible.field = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control my-3'}))
            else:
                visible.field = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control my-3'}))


RATING_CHOICES = [('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]


class ReviewForm(forms.Form):
    headline = forms.CharField(
        label='Titre',
        max_length=128,
        widget=forms.TextInput(attrs={'class': 'form-control my-3'}))
    rating = forms.ChoiceField(
        label='Notes',
        choices=RATING_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check form-check-inline'}))
    body = forms.CharField(
        label='Commentaire',
        max_length=8192,
        widget=forms.Textarea(attrs={'class': 'form-control my-3'}))


class AbonnementsForm(forms.Form):
    name = forms.CharField(label="Nom d'utilisateur", widget=forms.TextInput(attrs={'class': 'form-control my-3'}))
