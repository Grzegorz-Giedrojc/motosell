from django import forms

from .models import Oferta

class PostForm(forms.ModelForm):

    class Meta:
        model = Oferta
        fields = ('tytul', 'opis',)
